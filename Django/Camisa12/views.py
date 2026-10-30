from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from Camisa12.models import NotaConservacao, Time, Produto

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

    contexto = {
        "produto": produto,
    }

    return render(
        request,
        "produto_detalhe.html",
        contexto
    )
    