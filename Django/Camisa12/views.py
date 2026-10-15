from django.shortcuts import render
from Camisa12.models import NotaConservacao

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
