from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .repository import *

# Create your views here.
def index(request):
    return HttpResponse("<h1>Index</h1>")

def teleconsultores(request):
    listaDeTeleconsultores = Teleconsultor.objects.all()

    return render(request, 'teleconsultor_list.html', {'teleconsultores': listaDeTeleconsultores})

def solicitantes(request):
    listaDeSolicitante = RepositorioDeSolicitantes().obtemTodosSolicitantes()
    return render(request, 'solicitante_list.html', {'solicitantes': listaDeSolicitante})

def solicitantes_detail(request, solicitanteId):
    solicitante = RepositorioDeSolicitantes().obtemSolicitantesPorId(solicitanteId)
    return render(request, 'solicitante_form.html', {'solicitante': solicitante})



def solicitacoes(request):
    listaDeSolicitacoes = Solicitacao.objects.all()

    return render(request, 'solicitacao_list.html', {'solicitacoes': listaDeSolicitacoes})
