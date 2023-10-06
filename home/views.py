from django.shortcuts import render
from rest_framework import viewsets
from home.serializers import TopicoSerializer
from home.models import Topico


# Create your views here.
def home(request):
    contexto = {
        'title' : 'Home | Dream Tenis',
        'fotos' : Topico.objects.all(),
    }
    return render(
        request,
        'home/index.html',
        contexto
    )


def sessao(request):
       
    if request.method == 'POST':
        # Obtém o valor do campo de formulário
        sessao = request.POST.get('usuario')
        if sessao == 'Bárbara':
            sessao = 'Administrador'


        # Define a chave na sessão com o valor obtido
        request.session['login'] = sessao


    return render(
        request,
        'home/sessao.html',
    )


def exibir_valor(request):


    # Obtenha o valor da sessão
    # Defina um valor padrão se a sessão estiver vazia
    login = request.session.get('login', 'Nenhum valor definido')  
   
    contexto = {'login': login}
   
    return render(
        request,
        'home/exibir_valor.html',
        contexto,
    )

def encerrar_sessao(request):
    # Use o método clear() para limpar todos os dados da sessão
    request.session.clear()


    return exibir_valor(request)

class TopicoViewSet(viewsets.ModelViewSet):
    queryset = Topico.objects.all()
    serializer_class = TopicoSerializer