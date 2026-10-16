from django.contrib import admin
from django.forms import models
from .models import equipe, atleta, modalidade, tecnico

admin.site.register(modalidade)
admin.site.register(tecnico)
admin.site.register(equipe)
admin.site.register(atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'equipe')
    list_filter = ('modalidade', 'equipe')
    search_fields = ('nome')


    


