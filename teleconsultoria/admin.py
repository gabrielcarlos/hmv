from django.contrib import admin
from .models import Solicitante
from .models import Solicitacao
from .models import Teleconsultor
# Register your models here.

admin.site.register(Solicitacao)
admin.site.register(Teleconsultor)
admin.site.register(Solicitante)
