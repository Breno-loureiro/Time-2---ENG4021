import uuid
import pandas as pd
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from core.models import NotaConservacao, Produto, Tamanho, Time


class Command(BaseCommand):
  help = (
      'Importa produtos da planilha na raiz, gera códigos e sincroniza abas.'
  )

  def add_arguments(self, parser):
    # Argumento para o nome da planilha na raiz (ex: produtos.xlsx)
    parser.add_argument(
        'excel_filename',
        type=str,
        help='Nome do arquivo Excel localizado na raiz do projeto',
    )
    # Argumento opcional para escolher o banco de dados
    parser.add_argument(
        '--database',
        type=str,
        default='default',
        help='Nome da base de dados configurada em DATABASES',
    )

  def handle(self, *args, **options):
    excel_filename = options['excel_filename']
    db_name = options['database']

    self.stdout.write(
        self.style.WARNING(
            f'Lendo o arquivo "{excel_filename}" para a base de dados:'
            f' "{db_name}"...'
        )
    )

    try:
      # Como o terminal é executado na raiz onde está o manage.py,
      # o nome do arquivo já aponta diretamente para a raiz do projeto.
      excel_path = excel_filename

      # -------------------------------------------------------------
      # PASSO 1: Atualizar abas auxiliares no Excel
      # -------------------------------------------------------------
      with pd.ExcelWriter(
          excel_path, engine='openpyxl', mode='a', if_sheet_exists='replace'
      ) as writer:
        # Categorias
        categorias_data = [
            {'Categoria': cat[0], 'Descricao': cat[1]}
            for cat in Produto.CATEGORIAS
        ]
        pd.DataFrame(categorias_data).to_excel(
            writer, sheet_name='Categorias', index=False
        )

        # Tamanhos
        tamanhos_data = [
            {'Nome': t.nome, 'Largura': t.largura, 'Altura': t.altura}
            for t in Tamanho.objects.using(db_name).all()
        ]
        df_tamanhos = pd.DataFrame(tamanhos_data)
        if not df_tamanhos.empty:
          df_tamanhos.to_excel(writer, sheet_name='Tamanhos', index=False)

        # Notas de Conservação
        notas_data = [
            {
                'Nota': n.nota,
                'Titulo': n.titulo,
                'Descricao': n.descricao,
            }
            for n in NotaConservacao.objects.using(db_name).all()
        ]
        df_notas = pd.DataFrame(notas_data)
        if not df_notas.empty:
          df_notas.to_excel(
              writer, sheet_name='NotasConservacao', index=False
          )

      # -------------------------------------------------------------
      # PASSO 2: Ler a aba principal de Produtos e processar a importação
      # -------------------------------------------------------------
      df_produtos = pd.read_excel(excel_path, sheet_name=0)

      if 'Codigo' not in df_produtos.columns:
        df_produtos['Codigo'] = None

      contador = 0
      for index, row in df_produtos.iterrows():
        if pd.isna(row.get('Nome')):
          continue

        # Gerar código identificador se não existir
        codigo_atual = row.get('Codigo')
        if pd.isna(codigo_atual) or str(codigo_atual).strip() == '':
          codigo_gerado = f'SKU-{uuid.uuid4().hex[:6].upper()}'
          df_produtos.at[index, 'Codigo'] = codigo_gerado
        else:
          codigo_gerado = str(codigo_atual).strip()

        # Resolver Chaves Estrangeiras no banco correto
        tamanho_obj = None
        if pd.notna(row.get('Tamanho')):
          tamanho_obj, _ = Tamanho.objects.using(db_name).get_or_create(
              nome=str(row['Tamanho']).strip()
          )

        conservacao_obj = None
        if pd.notna(row.get('NotaConservacao')):
          conservacao_obj, _ = NotaConservacao.objects.using(db_name).get_or_create(
              nota=int(row['NotaConservacao'])
          )

        time_obj = None
        if pd.notna(row.get('Time')):
          time_obj, _ = Time.objects.using(db_name).get_or_create(
              nome=str(row['Time']).strip()
          )

        vendedor_obj = None
        if pd.notna(row.get('VendedorUsername')):
          vendedor_obj, _ = User.objects.using(db_name).get_or_create(
              username=str(row['VendedorUsername']).strip()
          )
        else:
          vendedor_obj = User.objects.using(db_name).first()

        if not vendedor_obj:
          continue

        # Criar ou atualizar o Produto no banco selecionado
        Produto.objects.using(db_name).update_or_create(
            nome=row['Nome'],
            defaults={
                'categoria': row.get('Categoria', 'FUTEBOL'),
                'marca': str(row.get('Marca', '')),
                'modelo': str(row.get('Modelo', '')),
                'ano': int(row['Ano']) if pd.notna(row.get('Ano')) else None,
                'descricao': str(row.get('Descricao', ''))
                + f' [Cod: {codigo_gerado}]',
                'preco': float(row['Preco']),
                'imagem': str(row.get('Imagem', '')),
                'ativo': bool(row.get('Ativo', True)),
                'tamanho': tamanho_obj,
                'conservacao': conservacao_obj,
                'time': time_obj,
                'vendedor': vendedor_obj,
            },
        )
        contador += 1

      # -------------------------------------------------------------
      # PASSO 3: Salvar de volta a aba de Produtos no Excel
      # -------------------------------------------------------------
      with pd.ExcelWriter(
          excel_path, engine='openpyxl', mode='a', if_sheet_exists='replace'
      ) as writer:
        df_produtos.to_excel(writer, sheet_name='Produtos', index=False)

      self.stdout.write(
          self.style.SUCCESS(
              f'Sucesso! {contador} produtos importados para o banco'
              f' "{db_name}". Planilha atualizada!'
          )
      )

    except Exception as e:
      self.stdout.write(
          self.style.ERROR(f'Erro durante o processo: {str(e)}')
      )