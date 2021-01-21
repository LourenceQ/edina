from django.shortcuts import render
from django.http import HttpResponse
from .models import usuario

# Create your views here.
def index(request):
    return render(request,'clinica/index.html')

def aconselhamento(request):
    return render(request,'clinica/aconselhamento.html')

def agua_magnetizada_saude(request):
    return render(request,'clinica/agua_magnetizada_saude.html')

def agua_magnetizada(request):
    return render(request,'clinica/agua_magnetizada.html')

def arteterapia(request):
    return render(request,'clinica/arteterapia.html')

def constelacao_familiar(request):
    return render(request,'clinica/constelacao_familiar.html')

def galeria(request):
    return render(request,'clinica/galeria.html')

def introducao_constelacao_familiar(request):
    return render(request,'clinica/introducao_constelacao_familiar.html')

def loja(request):
    return render(request,'clinica/loja.html')

def mandalas(request):
    return render(request,'clinica/mandalas.html')

def meditacao_mentalizacao(request):
    return render(request,'clinica/meditacao_mentalizacao.html')

def pnl(request):
    return render(request,'clinica/pnl.html')

def quemsomos(request):
    return render(request,'clinica/quemsomos.html')

def desenvolvimento_pessoal(request):
    return render(request,'clinica/desenvolvimento_pessoal.html')
