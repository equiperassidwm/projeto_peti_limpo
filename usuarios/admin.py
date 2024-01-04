from django.contrib import admin
from .models import UsuarioComplemento, UserAddress
from .forms.forms import UsuarioComplementoCreationForm, UsuarioComplementoUserChangeForm # importando o modelo de formulario de criaçao de usuario 
from django.contrib.auth.admin import UserAdmin # importando o administrador do usuario

# Register your models here.
class UsuarioComplementoAdmin(UserAdmin): # criando uma classe que herda de UserAdmin
    add_form_template = None # remove o template de formulario de ediçao personalizado
    add_form = UsuarioComplementoCreationForm # define define o formulario personalizado para adicionar usuarios
    form = UsuarioComplementoUserChangeForm # define o formulario personalizado para alterar usuarios
    model = UsuarioComplemento # o modelo a ser administrado por est UsuarioComplementoAdmin é o meu modelo UsuarioComplemento

    # campos a serem exibidos ao adicionar um novo usuário
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'first_name',
                    'last_name',
                    'cpf',
                    'telefone',
                    'email',
                    'username',
                    'password1',
                    'password2'
                ),
            },
        ),
    )

    # campos a serem exibidos ao editar um usuario
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Complemento do Usuário',
            {
                'fields': (
                    'cpf',
                    'telefone',
                )
            },
        ),
    )


admin.site.register(UsuarioComplemento, UsuarioComplementoAdmin)
admin.site.register(UserAddress)