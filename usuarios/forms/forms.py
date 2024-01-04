from django import forms # importando o formulario
from django.contrib.auth.forms import UserCreationForm, UserChangeForm # importando o formulário de criação de usuario
from ..models import UsuarioComplemento # importando o nosso modelo de usuario complementar


class UsuarioComplementoCreationForm(UserCreationForm): # criando uma classe para definir o formulario que herda no do formulario de criaçao de usuario
    class Meta: # vamos definir o modelo da classe
        model = UsuarioComplemento # referenciando o nosso modelo UsuarioComplemento
        fields = '__all__' # definindo que todos os campos da tabela UsuarioComplemento serão exibidos na criação do usuario


class UsuarioComplementoUserChangeForm(UserChangeForm):
    class Meta:
        model = UsuarioComplemento
        fields = '__all__'