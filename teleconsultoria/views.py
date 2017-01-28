from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Index</h1>")

def teleconsultor(request):
    return render(request, 'teleconsultor_list.html', {})

def solicitante(request):
    return render(request, 'solicitante_list.html', {})

def solicitacao(request):
    return render(request, 'solicitacao_list.html', {})
