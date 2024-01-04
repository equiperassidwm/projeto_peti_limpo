from django.urls import path
from . import views

urlpatterns = [
    path('solicitacao_agendamento/', views.solicitacao_agendamento, name='solicitacao_agendamento'),
    path('concluir_agendamento/', views.concluir_agendamento, name='concluir_agendamento'),
    path('lista_agendamentos/', views.lista_agendamentos, name='lista_agendamentos')
]
