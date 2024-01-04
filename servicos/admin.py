from django.contrib import admin
from .models import TipoServico, PorteAnimal, Preco, Animal, Agendamento

# Register your models here.
admin.site.register(TipoServico)
admin.site.register(PorteAnimal)
admin.site.register(Preco)
admin.site.register(Animal)
admin.site.register(Agendamento)