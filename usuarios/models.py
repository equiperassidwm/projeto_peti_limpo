from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UsuarioComplemento(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=16)
    data_criacao = models.DateTimeField(auto_now=True)

    def get_data_criacao(self):
        return self.data_criacao.strftime('%d/%m/%Y as %H:%M hs')
    
    
    
class UserAddress(models.Model):
    usuario_complemento = models.OneToOneField(UsuarioComplemento, on_delete=models.CASCADE)
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    
    def __str__(self):
        return f'{self.usuario_complemento.first_name} {self.usuario_complemento.last_name} | CEP: {self.cep } | {self.logradouro} | {self.complemento} | {self.bairro} | {self.cidade} | {self.uf}'

