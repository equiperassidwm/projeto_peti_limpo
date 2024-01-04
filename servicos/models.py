from django.db import models
from usuarios.models import UsuarioComplemento
from datetime import datetime

# Create your models here.
class TipoServico(models.Model):
    nome = models.CharField(max_length=50)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    

class PorteAnimal(models.Model):
    tipo = models.CharField(max_length=50)
    
    def __str__(self):
        return self.tipo
    

class Preco(models.Model):
    tipo_servico = models.ForeignKey(TipoServico, on_delete=models.CASCADE)
    porte_animal = models.ForeignKey(PorteAnimal, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.tipo_servico} | {self.porte_animal} | {self.preco}'
    

class Animal(models.Model):
    nome = models.CharField(max_length=50, default='Nome Padrão')
    tipo = models.CharField(max_length=50, default='Tipo Padrão')
    possui_alergia = models.BooleanField(default=False)
    qual_alergia = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return f'{self.nome} | {self.tipo} | {self.possui_alergia} | {self.qual_alergia}'
    

class Agendamento(models.Model):
    usuario_id = models.ForeignKey(UsuarioComplemento, on_delete=models.CASCADE)
    tipo_servico_id = models.ForeignKey(TipoServico, on_delete=models.CASCADE)
    porte_animal_id = models.ForeignKey(PorteAnimal, on_delete=models.CASCADE)
    preco_id = models.ForeignKey(Preco, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    data_agendamento = models.DateTimeField(default=datetime.now())

    def get_data_agendamento(self):
        return self.data_agendamento.strftime('%d/%m/%Y as %H:%M hs')
    
    def __str__(self):
        return f'Nome de Usuário: {self.usuario_id.username} | Nome do Animal: {self.animal.nome} | Tipo do Animal: {self.animal.tipo} | Tipo de Servico: {self.tipo_servico_id.nome} | Porte do Animal: {self.porte_animal_id.tipo} | Possui Alergia: {self.animal.possui_alergia} | Qual: {self.animal.qual_alergia} | Preço: {self.preco_id.preco} | Data do Agendamento: {self.data_agendamento}'