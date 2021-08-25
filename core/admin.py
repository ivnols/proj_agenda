from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventoAdmin (admin.ModelAdmin): #o evento criado na agenda vai ter esses rótulos abaixo
    list_display = ('id','titulo', 'data_evento', 'data_criacao')
    list_filter = ('titulo','usuario','data_evento', ) #criar um filtro ali do ladinho

admin.site.register(Evento, EventoAdmin)