from django.contrib import admin

# Register your models here.

from Camisa12.models import Tamanho
admin.site.register(Tamanho)

from Camisa12.models import NotaConservacao
admin.site.register(NotaConservacao)

from Camisa12.models import Time
admin.site.register(Time)

from Camisa12.models import Liga
admin.site.register(Liga)

from Camisa12.models import Confederacao
admin.site.register(Confederacao)

from Camisa12.models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):

    list_display = (
        "nome",
        "categoria",
        "preco",
        "time",
        "tamanho",
        "vendedor",
        "ativo",
    )

    list_filter = (
        "categoria",
        "ativo",
        "tamanho",
        "conservacao",
    )

    search_fields = (
        "nome",
        "marca",
        "modelo",
        "time__nome",
        "vendedor__username",
    )

    ordering = (
        "-criado_em",
    )

from Camisa12.models import Loja, Oferta, Avaliacao


@admin.register(Loja)
class LojaAdmin(admin.ModelAdmin):
    list_display = ("nome", "especialidade", "verificada")
    list_filter = ("verificada",)
    search_fields = ("nome",)


@admin.register(Oferta)
class OfertaAdmin(admin.ModelAdmin):
    list_display = ("produto", "loja", "preco", "frete")
    list_filter = ("loja",)
    search_fields = ("produto__nome", "loja__nome")


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ("produto", "usuario", "nota", "criado_em")
    list_filter = ("nota",)
    search_fields = ("produto__nome", "usuario__username", "comentario")


# Permite cadastrar as ofertas das lojas direto na tela do produto
class OfertaInline(admin.TabularInline):
    model = Oferta
    extra = 1


ProdutoAdmin.inlines = [OfertaInline]
