from django import forms 
from ..models import UsuarioComplemento, UserAddress
from django.contrib.auth.password_validation import validate_password
from django.contrib.messages import constants
from django.contrib import messages
from django.core.exceptions import ValidationError

class UsuarioComplementoForm(forms.ModelForm):
    class Meta:
        model = UsuarioComplemento
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmar_senha = cleaned_data.get('confirmar_senha')
        if password != confirmar_senha:
            raise ValidationError('As Senhas não são iguais!')
        cpf = self.cleaned_data.get('cpf')
        if UsuarioComplemento.objects.filter(cpf=cpf).exists():
            raise ValidationError('Já existe um cadastro com este CPF!')
        email = self.cleaned_data.get('email')
        if UsuarioComplemento.objects.filter(email=email).exists():
            raise ValidationError('Já existe um cadastro com este E-mail!')
        username = self.cleaned_data.get('usuario')
        if UsuarioComplemento.objects.filter(username=username).exists():
            raise ValidationError('Já existe um cadastro com este Nome de Usuário!')


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = "__all__"
