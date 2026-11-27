from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from Camisa12.forms import CadastroUsuarioForm, ProdutoForm, AvaliacaoForm
from Camisa12.models import NotaConservacao, Time, Produto, Avaliacao, Oferta

# Create your views here.

def notas(request):
    '''
    Busca todas as notas de conservação no banco de dados
    e mostra na página notas.html
    '''
    notas = NotaConservacao.objects.all()
    contexto = {
        'notas': notas,
    }
    return render(request, 'notas.html', contexto)

def busca_times(request):
    '''
    Mostra todos os times e permite buscar um time pelo nome.
    Usa a página times.html
    '''
    if request.method == 'GET':
        times = Time.objects.all()
        contexto = {
            'times': times,
        }
    else:
        search_query = request.POST.get('search')
        # filtra os times que tenham o texto buscado no nome
        times = Time.objects.filter(nome__icontains=search_query)
        contexto = {
            'search_query': search_query,   # o texto pesquisado
            'times': times,                 # os resultados da pesquisa
        }
    return render(request, 'times.html', contexto)

def cadastro(request):
    if request.user.is_authenticated:
        return redirect("Camisa12:minha_conta")

    if request.method == "POST":
        form = CadastroUsuarioForm(request.POST)

        if form.is_valid():
            usuario = form.save()

            # Faz login automaticamente depois do cadastro
            login(request, usuario)

            messages.success(
                request,
                "Conta criada com sucesso!"
            )

            return redirect("Camisa12:minha_conta")

    else:
        form = CadastroUsuarioForm()

    contexto = {
        "form": form,
    }

    return render(request, "cadastro.html", contexto)

def entrar(request):
    if request.user.is_authenticated:
        return redirect("Camisa12:minha_conta")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:

            login(request, usuario)

            messages.success(
                request,
                "Login realizado com sucesso!"
            )

            return redirect("Camisa12:minha_conta")

        else:

            messages.error(
                request,
                "Nome de usuário ou senha inválidos."
            )

    return render(request, "login.html")

def sair(request):
    if request.method == "POST":
        logout(request)

        messages.success(
            request,
            "Você saiu da sua conta."
        )

    return redirect("Camisa12:login")

@login_required(login_url="Camisa12:login")
def minha_conta(request):

    contexto = {
        "usuario": request.user,
    }

    return render(
        request,
        "minha_conta.html",
        contexto
    )

def produtos(request):

    produtos = Produto.objects.filter(
        ativo=True
    )

    busca = request.GET.get(
        "busca",
        ""
    ).strip()

    categoria = request.GET.get(
        "categoria",
        ""
    ).strip()


    if busca:

        produtos = produtos.filter(
            nome__icontains=busca
        )


    if categoria:

        produtos = produtos.filter(
            categoria=categoria
        )


    contexto = {

        "produtos": produtos,

        "busca": busca,

        "categoria": categoria,

        "categorias": Produto.CATEGORIAS,

    }


    return render(
        request,
        "produtos.html",
        contexto
    )

def produto_detalhe(request, produto_id):

    produto = get_object_or_404(
        Produto,
        id=produto_id,
        ativo=True
    )

    # Comparação de preços: ofertas das lojas, da mais barata para a mais cara
    ofertas = list(produto.ofertas.select_related("loja"))
    ofertas.sort(key=lambda oferta: oferta.total)
    melhor_oferta = ofertas[0] if ofertas else None
    economia = None
    if len(ofertas) > 1:
        economia = ofertas[-1].total - ofertas[0].total

    # Avaliações do produto
    avaliacoes = produto.avaliacoes.select_related("usuario")
    resumo_produto = avaliacoes.aggregate(media=Avg("nota"), total=Count("id"))

    # Reputação do vendedor: média das avaliações de todos os produtos dele
    resumo_vendedor = Avaliacao.objects.filter(
        produto__vendedor=produto.vendedor
    ).aggregate(media=Avg("nota"), total=Count("id"))

    # Formulário de avaliação (só para quem está logado)
    minha_avaliacao = None
    if request.user.is_authenticated:
        minha_avaliacao = avaliacoes.filter(usuario=request.user).first()

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "Entre na sua conta para avaliar.")
            return redirect("Camisa12:login")

        if produto.vendedor == request.user:
            messages.error(request, "Você não pode avaliar o próprio anúncio.")
            return redirect("Camisa12:produto_detalhe", produto_id=produto.id)

        form = AvaliacaoForm(request.POST, instance=minha_avaliacao)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.produto = produto
            avaliacao.usuario = request.user
            avaliacao.save()
            messages.success(request, "Avaliação salva. Obrigado!")
            return redirect("Camisa12:produto_detalhe", produto_id=produto.id)
    else:
        form = AvaliacaoForm(instance=minha_avaliacao)

    contexto = {
        "produto": produto,
        "ofertas": ofertas,
        "melhor_oferta": melhor_oferta,
        "economia": economia,
        "avaliacoes": avaliacoes,
        "media_produto": resumo_produto["media"],
        "total_avaliacoes": resumo_produto["total"],
        "media_vendedor": resumo_vendedor["media"],
        "total_avaliacoes_vendedor": resumo_vendedor["total"],
        "form": form,
        "minha_avaliacao": minha_avaliacao,
    }

    return render(
        request,
        "produto_detalhe.html",
        contexto
    )

@login_required(login_url="Camisa12:login")
def cadastrar_produto(request):

    if request.method == "POST":
        form = ProdutoForm(request.POST)

        if form.is_valid():
            produto = form.save(commit=False)

            # O vendedor é sempre o usuário logado
            produto.vendedor = request.user

            produto.ativo = True
            produto.save()

            messages.success(
                request,
                "Produto cadastrado com sucesso!"
            )

            return redirect("Camisa12:meus_anuncios")

    else:
        form = ProdutoForm()

    contexto = {
        "form": form,
        "titulo": "Cadastrar produto",
        "texto_botao": "Cadastrar produto",
    }

    return render(
        request,
        "formulario_produto.html",
        contexto
    )

@login_required(login_url="Camisa12:login")
def meus_anuncios(request):

    anuncios = Produto.objects.filter(
        vendedor=request.user
    ).select_related(
        "time",
        "tamanho",
        "conservacao"
    ).order_by("-criado_em")

    total = anuncios.count()

    ativos = anuncios.filter(
        ativo=True
    ).count()

    inativos = total - ativos

    contexto = {
        "anuncios": anuncios,
        "total": total,
        "ativos": ativos,
        "inativos": inativos,
    }

    return render(
        request,
        "meus_anuncios.html",
        contexto
    )

@login_required(login_url="Camisa12:login")
def editar_produto(request, produto_id):

    produto = get_object_or_404(
        Produto,
        id=produto_id,
        vendedor=request.user
    )

    if request.method == "POST":
        form = ProdutoForm(
            request.POST,
            instance=produto
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Anúncio atualizado com sucesso!"
            )

            return redirect("Camisa12:meus_anuncios")

    else:
        form = ProdutoForm(instance=produto)

    contexto = {
        "form": form,
        "titulo": "Editar anúncio",
        "texto_botao": "Salvar alterações",
        "produto": produto,
    }

    return render(
        request,
        "formulario_produto.html",
        contexto
    )


def catalogo_futebol(request):
    busca = request.GET.get("busca", "").strip()

    produtos = Produto.objects.filter(
        categoria="FUTEBOL",
        ativo=True
    ).select_related(
        "time",
        "vendedor"
    ).order_by("-criado_em")

    if busca:
        produtos = produtos.filter(
            nome__icontains=busca
        )

    destaque = Produto.objects.filter(
        categoria="FUTEBOL",
        ativo=True
    ).select_related(
        "time",
        "vendedor",
        "tamanho",
        "conservacao"
    ).order_by("preco").first()
    contexto = {
        "produtos": produtos,
        "total": produtos.count(),
        "busca": busca,
        "destaque": destaque,
    }

    return render(
        request,
        "futebol.html",
        contexto
    )


def catalogo_nba(request):
    busca = request.GET.get("busca", "").strip()

    produtos = Produto.objects.filter(
        categoria="NBA",
        ativo=True
    ).select_related(
        "time",
        "vendedor"
    ).order_by("-criado_em")

    if busca:
        produtos = produtos.filter(
            nome__icontains=busca
        )

    contexto = {
        "produtos": produtos,
        "total": produtos.count(),
        "busca": busca,
    }

    return render(request, "nba.html", contexto)


def catalogo_nfl(request):
    busca = request.GET.get("busca", "").strip()

    produtos = Produto.objects.filter(
        categoria="NFL",
        ativo=True
    ).select_related(
        "time",
        "vendedor"
    ).order_by("-criado_em")

    if busca:
        produtos = produtos.filter(
            nome__icontains=busca
        )

    contexto = {
        "produtos": produtos,
        "total": produtos.count(),
        "busca": busca,
    }

    return render(request, "nfl.html", contexto)

def catalogo_chuteiras(request):
    busca = request.GET.get("busca", "").strip()

    produtos = Produto.objects.filter(
        categoria="CHUTEIRAS",
        ativo=True
    ).select_related(
        "time",
        "vendedor"
    ).order_by("-criado_em")

    if busca:
        produtos = produtos.filter(
            nome__icontains=busca
        )

    contexto = {
        "produtos": produtos,
        "total": produtos.count(),
        "busca": busca,
    }

    return render(request, "chuteiras.html", contexto)

def catalogo_acessorios(request):
    busca = request.GET.get("busca", "").strip()

    produtos = Produto.objects.filter(
        categoria="ACESSORIOS",
        ativo=True
    ).select_related(
        "time",
        "vendedor"
    ).order_by("-criado_em")

    if busca:
        produtos = produtos.filter(
            nome__icontains=busca
        )

    contexto = {
        "produtos": produtos,
        "total": produtos.count(),
        "busca": busca,
    }

    return render(request, "acessorios.html", contexto)

def termos_uso(request):
    return render(request, 'termos_uso.html')


def oferta_detalhe(request, oferta_id):

    oferta = get_object_or_404(
        Oferta.objects.select_related("produto", "produto__time", "loja"),
        id=oferta_id,
        produto__ativo=True
    )
    produto = oferta.produto

    # As outras lojas que vendem o mesmo produto, para comparar
    outras = list(
        produto.ofertas.select_related("loja").exclude(id=oferta.id)
    )
    todas = sorted(outras + [oferta], key=lambda o: o.total)
    posicao = todas.index(oferta) + 1
    diferenca = oferta.total - todas[0].total

    # Outros produtos dessa mesma loja
    mais_da_loja = oferta.loja.ofertas.select_related("produto").filter(
        produto__ativo=True
    ).exclude(produto=produto)[:4]

    contexto = {
        "oferta": oferta,
        "produto": produto,
        "outras": sorted(outras, key=lambda o: o.total),
        "posicao": posicao,
        "total_ofertas": len(todas),
        "diferenca": diferenca,
        "mais_da_loja": mais_da_loja,
    }

    return render(
        request,
        "oferta_detalhe.html",
        contexto
    )
