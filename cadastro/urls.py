from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro, name='cadastro'),
    path('gravar/', views.gravar, name='gravar'),
    path('mostrar/',views.exibe,name='mostrar'),
    path('mostrar2/',views.exibe2,name='mostrar2'),
    path('apagar/<int:id>',views.apagar,name='apagar'),
    path('editar/<int:id>',views.editar,name='editar'),
    path('atualizar/<int:id>',views.atualizar,name='atualizar'),
    path('apagar2/<int:id>',views.apagar2,name='apagar2'),
    path('editar2/<int:id>',views.editar2,name='editar2'),
    path('atualizar2/<int:id>',views.atualizar2,name='atualizar2'),
    path('localizar/',views.localizar,name='localizar'),
]
