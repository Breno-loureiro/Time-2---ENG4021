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
