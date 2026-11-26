from django.contrib import admin
from django.urls import path

from Camisa12 import views
from django.views.generic import TemplateView

app_name = "Camisa12"


urlpatterns = [

    # Administração
    path("admin/", admin.site.urls),


    # Funcionalidades que já existiam
    path(
        "notas/",
        views.notas,
        name="notas"
    ),

    path(
        "times/",
        views.busca_times,
        name="busca_times"
    ),


    # Usuários
    path(
        "cadastro/",
        views.cadastro,
        name="cadastro"
    ),

    path(
        "login/",
        views.entrar,
        name="login"
    ),

    path(
        "logout/",
        views.sair,
        name="logout"
    ),

    path(
        "minha-conta/",
        views.minha_conta,
        name="minha_conta"
    ),


    # Produtos
    path(
        "produtos/",
        views.produtos,
        name="produtos"
    ),

    path(
        "produtos/<int:produto_id>/",
        views.produto_detalhe,
        name="produto_detalhe"
    ),
        path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("futebol/", views.catalogo_futebol, name="futebol"),
    path("nba/", views.catalogo_nba, name="nba"),
    path("nfl/", views.catalogo_nfl, name="nfl"),
    path("chuteiras/", views.catalogo_chuteiras, name="chuteiras"),
    path("acessorios/", views.catalogo_acessorios, name="acessorios"),
    path("sobre/", TemplateView.as_view(template_name="sobre.html"), name="sobre"),
    path("como-funciona/", TemplateView.as_view(template_name="como_funciona.html"), name="como_funciona"),
    path("guia-de-tamanhos/", TemplateView.as_view(template_name="guia_tamanhos.html"), name="guia_tamanhos"),
    path("trocas-e-devolucoes/", TemplateView.as_view(template_name="trocas_devolucoes.html"), name="trocas_devolucoes"),
    path("central-de-ajuda/", TemplateView.as_view(template_name="central_ajuda.html"), name="central_ajuda"),
    path("fale-conosco/", TemplateView.as_view(template_name="fale_conosco.html"), name="fale_conosco"),
    path("lojas/", TemplateView.as_view(template_name="lojas.html"), name="lojas"),
    path("lancamento/", TemplateView.as_view(template_name="lancamento.html"), name="lancamento"),
    path("carrinho/", TemplateView.as_view(template_name="carrinho.html"), name="carrinho"),
    #Área do vendedor
    path(
        "meus-anuncios/",
        views.meus_anuncios,
        name="meus_anuncios"
    ),

    path(
        "cadastrar-produto/",
        views.cadastrar_produto,
        name="cadastrar_produto"
    ),

    path(
        "editar-produto/<int:produto_id>/",
        views.editar_produto,
        name="editar_produto"
    ),

    path(
        "termos-de-uso/",
        views.termos_uso,
        name="termos_uso"
    ),
]