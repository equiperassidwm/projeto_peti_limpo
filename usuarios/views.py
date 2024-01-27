from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.messages import constants, get_messages
from django.contrib import messages
from django.db import IntegrityError, transaction
from django.contrib.auth import authenticate, login, logout
from .models import UsuarioComplemento, UserAddress
from usuarios.forms.cadastro_forms import UsuarioComplementoForm, UserAddressForm



# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')

    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobre_nome = request.POST.get('sobre_nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cep = request.POST.get('cep')
        logradouro = request.POST.get('logradouro')
        complemento = request.POST.get('complemento')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        uf = request.POST.get('uf')
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')


        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'AS senhas não são iguais')
            return redirect('/usuarios/cadastro')
        
        if UsuarioComplemento.objects.filter(cpf=cpf).exists():
            messages.add_message(request, constants.ERROR, 'Ja existe um cadastro com este CPF!')
            return redirect('/usuarios/cadastro')
        
        if UsuarioComplemento.objects.filter(email=email).exists():
            messages.add_message(request, constants.ERROR, 'Ja existe um cadastro com este email!')
            return redirect('/usuarios/cadastro')
        
        if UsuarioComplemento.objects.filter(username=usuario).exists():
            messages.add_message(request, constants.ERROR, 'Este nome de usuário já existe!')
            return redirect('/usuarios/cadastro')

        if len(senha) < 8:
            messages.add_message(request, constants.ERROR, 'A senha deve ter no mínimo 8 caracteres!')
            return redirect('/usuarios/cadastro')

        try:
            # para tratar a criação do usuario e endereço com se fosse uma só
            with transaction.atomic():
                user = UsuarioComplemento.objects.create_user(
                    first_name=nome,
                    last_name=sobre_nome,
                    cpf=cpf,
                    email=email,
                    telefone=telefone,
                    username=usuario,
                    password=senha,
                )
                
                endereco = UserAddress.objects.create(
                    usuario_complemento=user,
                    cep=cep,
                    logradouro=logradouro,
                    complemento=complemento,
                    bairro=bairro,
                    cidade=cidade,
                    uf=uf
                )
                
                messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
                return redirect('/usuarios/user_login')
            
        except IntegrityError as e:
            messages.add_message(request, constants.ERROR, f'{str(e)} Erro ao cadastrar o Usuário ou o Endereço!')
            return redirect('/usuarios/cadastro')

def logar(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(request, username=usuario, password=senha)
        if user:
            login(request, user)
            return redirect('/')
        
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha incorreto, tente novamente!')
            return redirect('/usuarios/user_login')
        

def deslogar(request):
    logout(request)
    return redirect('/')


