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