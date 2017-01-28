from django.db import models
from django.utils import timezone
from .models import *

class RepositorioDeSolicitantes(models.Model):
    def obtemTodosSolicitantes(self):
        return Solicitante.objects.all()

    def obtemSolicitantesPorId(self, solicitanteId):
        return Solicitante.objects.get(id=solicitanteId)