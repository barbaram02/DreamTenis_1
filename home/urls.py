from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='principal'),
    path('sessao/', views.sessao,name='sessao'),
    path('exibir_valor/', views.exibir_valor, name='exibir_valor'),
    path('encerrar/', views.encerrar_sessao, name='encerrar'),
]
