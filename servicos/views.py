from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TipoServico, PorteAnimal, Preco, Animal, Agendamento
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.messages import constants
from django.contrib import messages
from datetime import datetime


   

# Create your views here.
@login_required
def solicitacao_agendamento(request):
    tipo_servico = TipoServico.objects.all()
    porte_animal = PorteAnimal.objects.all()
    preco = Preco.objects.all()
    animal = Animal.objects.all()

    if request.method == 'GET':
        return render(request, 'solicitacao_agendamento.html', {'tipo_servico': tipo_servico, 'porte_animal': porte_animal, 'preco': preco, 'animal': animal})
    
    
    elif request.method == 'POST':
        usuario = request.user
        tipo_servico_id = request.POST.getlist('servicos')
        porte_do_animal = request.POST.get('porte')
        nome_animal = request.POST.get('nome_animal')
        tipo_animal = request.POST.get('tipo_animal')
        possui_alergia = request.POST.get('opcao')
        qual = request.POST.get('alergia')
        data_agendamento = request.POST.get('data_agendamento')

        if not tipo_servico_id:
            messages.add_message(request, constants.ERROR, 'Selecione o Tipo do Serviço')
            return redirect('/servicos/solicitacao_agendamento')

        if not nome_animal:
            messages.add_message(request, constants.ERROR, 'Digite o Nome do animal')
            return redirect('/servicos/solicitacao_agendamento')

        if not tipo_animal:
            messages.add_message(request, constants.ERROR, 'Digite o Tipo do animal')
            return redirect('/servicos/solicitacao_agendamento')
        
        # verificação para o campo do type radio
        if possui_alergia not in ['Sim','Não']:
            messages.add_message(request, constants.ERROR, 'Marque Sim ou Nao para a pergunta "Possui Alergia?"')
            return redirect('/servicos/solicitacao_agendamento')
        # se o campo possui_alergia for sim e o campo qual estiver vazio retorna erro
        elif possui_alergia == 'Sim' and not qual:
            messages.add_message(request, constants.ERROR, 'Descreva qual o tipo de alergia do seu animal')
            return redirect('/servicos/solicitacao_agendamento')

        
        if not data_agendamento:
            messages.add_message(request, constants.ERROR, 'Selecione a Data do Agendamento')
            return redirect('/servicos/solicitacao_agendamento')

        solicitacao_tipo_servico = TipoServico.objects.filter(id__in=tipo_servico_id) # é uma lista
        porte = PorteAnimal.objects.get(id=porte_do_animal) # é so um 
        precos = Preco.objects.filter(tipo_servico__in=solicitacao_tipo_servico, porte_animal=porte)

        preco_total = 0
        for tipo in solicitacao_tipo_servico:
            if tipo.disponivel:
                for preco in precos:
                    if preco.tipo_servico.id == tipo.id:
                        valor = preco.preco
                        preco_total += valor
               
        data_objeto = datetime.strptime(data_agendamento, '%Y-%m-%dT%H:%M') # pegando o objeto da data no estilo americano
        data_agendamento = data_objeto.strftime('%d/%m/%Y as %H:%M hs') # convertendo o objeto para estilo brasileiro

        return render(request, 'solicitacao_agendamento.html', {'usuario': usuario,'solicitacao_tipo_servico': solicitacao_tipo_servico, 'precos': precos, 'tipo_servico': tipo_servico,'porte': porte, 'nome_animal': nome_animal, 'tipo_animal': tipo_animal, 'possui_alergia': possui_alergia, 'qual': qual, 'data_agendamento': data_agendamento, 'preco_total': preco_total})


@login_required
def concluir_agendamento(request):
    
    if request.method == 'POST':
        usuario = request.user
        nome_animal = request.POST.get('nome_animal')
        tipo_animal = request.POST.get('tipo_animal')
        solicitacao_tipo_servico_ids = request.POST.getlist('tipo_servico')
        porte_animal_id = request.POST.get('porte_animal')
        data_agendamento = request.POST.get('data_agendamento')
        possui_alergia = request.POST.get('possui_alergia')
        qual = request.POST.get('qual')


        try:
            possui_alergia_bool = True if possui_alergia == 'Sim' else False

            data_agendamento_objeto = datetime.strptime(data_agendamento, '%d/%m/%Y as %H:%M hs')
            data_agendamento = data_agendamento_objeto.strftime('%Y-%m-%d %H:%M:%S')

            porte_animal = PorteAnimal.objects.get(id=porte_animal_id)

    
            animal = Animal.objects.create(
                nome=nome_animal,
                tipo=tipo_animal,
                possui_alergia=possui_alergia_bool,
                qual_alergia=qual
            )

            for tipo_servico_id in solicitacao_tipo_servico_ids:
                tipo_servico = TipoServico.objects.get(id=tipo_servico_id)
                preco = Preco.objects.get(tipo_servico=tipo_servico, porte_animal=porte_animal)

                agendamento = Agendamento.objects.create(
                    usuario_id=usuario,
                    animal = animal,
                    tipo_servico_id=tipo_servico,
                    porte_animal_id=porte_animal,
                    preco_id=preco,
                    data_agendamento=data_agendamento
                )
              
            messages.add_message(request, constants.SUCCESS, 'Solicitação de Serviços Agendada com Sucesso!')
            return redirect('/servicos/solicitacao_agendamento')
    
        except IntegrityError:
            messages.add_message(request, constants.ERROR, 'Erro ao criar o agendamento, contacte o administrador do sistema!')
            return redirect('/servicos/solicitacao_agendamento')
        
@login_required
def lista_agendamentos(request):
    usuario = request.user
    agendamentos = Agendamento.objects.filter(usuario_id=usuario) 
    return render(request, 'lista_agendamentos.html', {'agendamentos': agendamentos})

