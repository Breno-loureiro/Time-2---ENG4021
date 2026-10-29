from django.shortcuts import render
from Camisa12.models import NotaConservacao, Time

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
