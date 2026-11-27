"""
Cadastra produtos de demonstração no catálogo:
8 camisas de futebol, 8 da NBA, 8 da NFL, 5 chuteiras e 5 acessórios.

Os preços são fictícios (dados de demonstração). As fotos ficam vazias:
cole o link da imagem no admin (campo "Imagem") ou no dicionário abaixo.

Pode rodar mais de uma vez: produtos com o mesmo nome não são duplicados.

Uso:  python manage.py popular_produtos
"""
from decimal import Decimal

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from Camisa12.models import NotaConservacao, Produto, Tamanho, Time

# (time, sigla, liga, marca, modelo, preço)
FUTEBOL = [
    ("Corinthians", "COR", "Brasileirão Série A", "Nike", "Titular", "349.90"),
    ("Palmeiras", "PAL", "Brasileirão Série A", "Puma", "Titular", "349.90"),
    ("São Paulo", "SAO", "Brasileirão Série A", "New Balance", "Titular", "329.90"),
    ("Santos", "SAN", "Brasileirão Série A", "Umbro", "Titular", "319.90"),
    ("Grêmio", "GRE", "Brasileirão Série A", "Umbro", "Titular", "329.90"),
    ("Internacional", "INT", "Brasileirão Série A", "Adidas", "Titular", "339.90"),
    ("Vasco da Gama", "VAS", "Brasileirão Série A", "Kappa", "Titular", "299.90"),
    ("Botafogo", "BOT", "Brasileirão Série A", "Reebok", "Titular", "349.90"),
]

NBA = [
    ("Boston Celtics", "BOS", "Titular", "389.90"),
    ("Chicago Bulls", "CHI", "Titular", "379.90"),
    ("Miami Heat", "MIA", "Titular", "379.90"),
    ("Brooklyn Nets", "BKN", "Titular", "369.90"),
    ("Milwaukee Bucks", "MIL", "Titular", "379.90"),
    ("Denver Nuggets", "DEN", "Titular", "389.90"),
    ("Phoenix Suns", "PHX", "Titular", "379.90"),
    ("Philadelphia 76ers", "PHI", "Titular", "369.90"),
]

NFL = [
    ("Kansas City Chiefs", "KC", "Titular", "399.90"),
    ("San Francisco 49ers", "SF", "Titular", "399.90"),
    ("Philadelphia Eagles", "PHI", "Titular", "389.90"),
    ("Green Bay Packers", "GB", "Titular", "389.90"),
    ("Pittsburgh Steelers", "PIT", "Titular", "379.90"),
    ("Baltimore Ravens", "BAL", "Titular", "379.90"),
    ("Buffalo Bills", "BUF", "Titular", "379.90"),
    ("Las Vegas Raiders", "LV", "Titular", "379.90"),
]

# (nome, marca, modelo, descrição, preço)
CHUTEIRAS = [
    ("Chuteira Nike Mercurial Vapor Elite", "Nike", "Mercurial Vapor",
     "Chuteira de campo leve, feita para velocidade.", "899.90"),
    ("Chuteira Adidas Predator Elite", "Adidas", "Predator",
     "Chuteira de campo com foco em controle e precisão no chute.", "849.90"),
    ("Chuteira Puma Future Ultimate", "Puma", "Future",
     "Chuteira de campo com ajuste flexível para dribles e agilidade.", "799.90"),
    ("Chuteira Nike Phantom Elite", "Nike", "Phantom",
     "Chuteira de campo para jogadores de passe e construção de jogo.", "879.90"),
    ("Chuteira Adidas F50 Elite", "Adidas", "F50",
     "Chuteira de campo ultraleve para jogadores de velocidade.", "829.90"),
]

ACESSORIOS = [
    ("Bola Adidas Trionda Réplica", "Adidas", "Trionda",
     "Bola de futebol de campo, modelo réplica.", "249.90"),
    ("Caneleira Nike Mercurial Lite", "Nike", "Mercurial Lite",
     "Caneleira leve com proteção para jogos e treinos.", "89.90"),
    ("Luvas de Goleiro Adidas Predator", "Adidas", "Predator",
     "Luvas de goleiro com palma aderente.", "199.90"),
    ("Mochila Nike Brasilia", "Nike", "Brasilia",
     "Mochila esportiva para treinos e uso diário.", "179.90"),
    ("Meiões Nike Academy", "Nike", "Academy",
     "Meiões de futebol de cano alto, tecido respirável.", "59.90"),
]

TAMANHOS = ["P", "M", "G", "GG"]


class Command(BaseCommand):
    help = "Cadastra 8 camisas de futebol, 8 NBA, 8 NFL, 5 chuteiras e 5 acessórios de demonstração."

    def handle(self, *args, **options):
        vendedor = (
            User.objects.filter(is_superuser=True).order_by("id").first()
            or User.objects.order_by("id").first()
        )
        if vendedor is None:
            vendedor = User.objects.create_user(username="camisa12_loja")
            vendedor.set_unusable_password()
            vendedor.save()

        novo = NotaConservacao.objects.filter(nota=5).first()
        tamanhos = [Tamanho.objects.filter(nome=n).first() for n in TAMANHOS]

        criados = 0

        def cadastrar(nome, categoria, preco, defaults):
            nonlocal criados
            _, criado = Produto.objects.get_or_create(
                nome=nome,
                categoria=categoria,
                defaults={
                    "preco": Decimal(preco),
                    "ano": 2026,
                    "ativo": True,
                    "vendedor": vendedor,
                    "conservacao": novo,
                    **defaults,
                },
            )
            criados += int(criado)

        def camisa(indice, categoria, time_nome, sigla, liga, marca, modelo, preco):
            time, _ = Time.objects.get_or_create(
                nome=time_nome, defaults={"sigla": sigla, "liga": liga}
            )
            cadastrar(
                f"Camisa {time_nome} | 2026",
                categoria,
                preco,
                {
                    "marca": marca,
                    "modelo": modelo,
                    "descricao": f"Camisa {modelo.lower()} do {time_nome} (dados de demonstração).",
                    "time": time,
                    "tamanho": tamanhos[indice % len(tamanhos)],
                },
            )

        for i, (time, sigla, liga, marca, modelo, preco) in enumerate(FUTEBOL):
            camisa(i, "FUTEBOL", time, sigla, liga, marca, modelo, preco)
        for i, (time, sigla, modelo, preco) in enumerate(NBA):
            camisa(i, "NBA", time, sigla, "NBA", "Nike", modelo, preco)
        for i, (time, sigla, modelo, preco) in enumerate(NFL):
            camisa(i, "NFL", time, sigla, "NFL", "Nike", modelo, preco)

        for nome, marca, modelo, descricao, preco in CHUTEIRAS:
            cadastrar(nome, "CHUTEIRAS", preco,
                      {"marca": marca, "modelo": modelo, "descricao": descricao})
        for nome, marca, modelo, descricao, preco in ACESSORIOS:
            cadastrar(nome, "ACESSORIOS", preco,
                      {"marca": marca, "modelo": modelo, "descricao": descricao})

        self.stdout.write(self.style.SUCCESS(f"{criados} produtos novos cadastrados."))
