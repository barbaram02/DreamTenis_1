from django.db import models

# Create your models here.
class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    nascimento = models.DateField()
    cpf = models.TextField(max_length=11)
    email = models.EmailField(max_length=255)
    funcao = models.TextField(max_length=50)
    numero = models.TextField(max_length=11)
    unidade = models.TextField(max_length=100)

class Topico(models.Model):
    id   = models.AutoField(primary_key=True)
    tema = models.CharField(max_length=30)
    foto = models.ImageField()
    conteudo = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.tema