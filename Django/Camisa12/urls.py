from django.contrib import admin
from django.urls import path

from Camisa12 import views


app_name = "Camisa12"


urlpatterns = [

    # Administração
    path(
        "admin/",
        admin.site.urls
    ),


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

]