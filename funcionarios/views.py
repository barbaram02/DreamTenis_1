from django.shortcuts import render
from rest_framework import viewsets
from funcionarios.serializers import TopicoSerializer
from funcionarios.models import Topico


# Create your views here.
def funcionarios(request):
    contexto = {
        'title' : 'Nossos Funcionários | Dream Tenis',
        'fotos' : Topico.objects.all()
       
    }
    return render(
        request,
        'funcionarios/funcionarios.html',
        contexto
    )

class TopicoViewSet(viewsets.ModelViewSet):
    queryset = Topico.objects.all()
    serializer_class = TopicoSerializer