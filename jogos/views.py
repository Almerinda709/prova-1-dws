from django.shortcuts import render
from django.http import HttpResponse
from .models import equipe, atleta, modalidade, tecnico

# Create your views here.

class indexView:
    def index(request):
        return render(request, 'jogos/index.html')
