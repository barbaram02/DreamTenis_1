from django.shortcuts import render
from .models import Pessoa
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from cadastro.serializers import TopicoSerializer
from cadastro.models import Topico

# Create your views here.
@login_required
def cadastro(request):
    contexto = {
        'title' : 'Cadastro | Dream Tenis'
    }
    return render(
        request,
        'cadastro/cadastro.html',
        contexto
    )

def gravar(request):
    nome_error = nascimento_error = cpf_error = email_error = funcao_error = numero_error = unidade_error  = ''

    nome  = request.POST.get('nome')
    nascimento = request.POST.get('nascimento')
    cpf = request.POST.get('cpf')
    email = request.POST.get('email')
    funcao = request.POST.get('funcao')
    numero = request.POST.get('numero')
    unidade = request.POST.get('unidade')

    if not nome: 
        nome_error  = 'Adicionar Nome! '
    if Pessoa.objects.filter(nome=nome):
        nome_error = 'Nome duplicado! ' #Testando para não colocar nome repetido no banco de dados (duplicar)

    if not nascimento: 
        nascimento_error = 'Adicionar Data de Nascimento! '   

    if not cpf:
        cpf_error = 'Adicionar um CPF! '  
    if Pessoa.objects.filter(cpf=cpf):
        cpf_error = 'CPF duplicado! '

    if not email: 
        email_error = 'Email Inválido.'
    if Pessoa.objects.filter(email=email): #É um filtro para filtrar os dados no banco de dados
         email_error = 'Email duplicado! ' #Testando para não colocar email repetido no banco de dados (duplicar)

    if not funcao:
        funcao_error = 'Adicionar um Cargo! '

    if not numero:
        numero_error = 'Adicionar um Número! '
    
    if not unidade:
        unidade_error = 'Adicionar uma Unidade! '

    if nome_error or nascimento_error or cpf_error or email_error or funcao_error or numero_error or unidade_error :
        contexto = {
            'nome_error' : nome_error,
            'nascimento_error': nascimento_error,
            'cpf_error' : cpf_error,
            'email_error': email_error,
            'funcao_error' : funcao_error,
            'numero_error' : numero_error,
            'unidade_error' : unidade_error,
            'msg_error'  : nome_error+ ' ' +nascimento_error+ ' ' +email_error+ ' ' +cpf_error+ ' ' +funcao_error+ ' ' +numero_error+ ' ' + unidade_error,
            'nome'       : nome,
            'nascimento'      : nascimento,
            'cpf' : cpf,
            'email'      : email,
            'funcao' : funcao,
            'numero' : numero,
            'unidade' : unidade,
        }

        return render (
        request,
        'cadastro/cadastro.html',
        contexto,
        )
    
    nova_pessoa = Pessoa()
    nova_pessoa.nome  = nome
    nova_pessoa.nascimento = nascimento
    nova_pessoa.cpf = cpf
    nova_pessoa.email = email
    nova_pessoa.funcao = funcao
    nova_pessoa.numero = numero
    nova_pessoa.unidade = unidade
    nova_pessoa.save() #salva os dados na tabela

    #return contato(request) #retorna para a função contato
    return cadastro(request)


def exibe(request):
    exibe_pessoas = {
        'pessoas' : Pessoa.objects.all()
    }
    return render (
        request,
        'cadastro/mostrar.html',
        exibe_pessoas
    )

def apagar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.delete()
    return exibe(request)

def editar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    return render (
        request,
        'cadastro/editar.html',
        {"pessoa": pessoa}
    )

def atualizar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.nome  = request.POST.get('nome')
    pessoa.nascimento = request.POST.get('nascimento') 
    pessoa.cpf = request.POST.get('cpf')
    pessoa.email = request.POST.get('email')
    pessoa.funcao = request.POST.get('funcao')
    pessoa.numero = request.POST.get('numero')
    pessoa.unidade = request.POST.get('unidade')
    
    pessoa.save()
    return exibe(request)

@login_required
def exibe2(request):
    exibe2_pessoas = {
        'pessoas' : Pessoa.objects.all()
    }
    return render (
        request,
        'cadastro/mostrar2.html',
        exibe2_pessoas
    )

def apagar2(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.delete()
    return exibe2(request)

def editar2(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    return render (
        request,
        'cadastro/editar2.html',
        {"pessoa": pessoa}
    )

def atualizar2(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.nome  = request.POST.get('nome')
    pessoa.nascimento = request.POST.get('nascimento') 
    pessoa.cpf = request.POST.get('cpf')
    pessoa.email = request.POST.get('email')
    pessoa.funcao = request.POST.get('funcao')
    pessoa.numero = request.POST.get('numero')
    pessoa.unidade = request.POST.get('unidade')
    
    pessoa.save()
    return exibe2(request)


class TopicoViewSet(viewsets.ModelViewSet):
   queryset = Topico.objects.all()
   serializer_class = TopicoSerializer

def mostrar2_tabela(request):
    mostrar2_tabela = {
        'mostrar2_tabela' : Topico.objects.all()
    }
    return render (
        request,
        'cadastro/mostrar2_tabela.html',
        mostrar2_tabela
    )

@login_required
def localizar(request):
   contexto = {}
   erro = None

   if request.method =='POST':
        selecao = request.POST.get('tbusca')
        busca   = request.POST.get('busca')
        pessoas = [] #lista vazia
        try: #Realiza uma condição (Verifica se é um valor válido)
            if selecao == 'id':
                try:
                    pessoa = Pessoa.objects.get(id_pessoa=busca)
                    pessoas.append(pessoa)
                except ValueError:
                    erro = 'Informe para id um valor numérico'
                    
            elif selecao == 'nome':
                pessoas = Pessoa.objects.filter(nome=busca)
            elif selecao == 'email':
                pessoas = Pessoa.objects.filter(email=busca)
            
            if not pessoas: #verifique se a lista de pessoas está vazia
                raise Pessoa.DoesNotExist  #raise serve para forçar a excessão a funcionar (Fazendo uma excessão personalizada)
                #DoesNotExit não funciona com para filter! Quando usado o filter, temos que fazer uma excessão personalizada.
                #Pois o filter não verifica uma condição, apenas filtra os dados.

        except Pessoa.DoesNotExist: 
            if not erro: 
                erro = 'Registro não encontrado'

   else: # se for a primeira vez do carregamento
        pessoas = [] #Ao invés de pessoa é pessoas por ser lista
        busca = '' 
   contexto = {"pessoas": pessoas, "busca":busca, "erro":erro }
   return render(
        request,
        'cadastro/localizar.html',
        contexto,
    )

