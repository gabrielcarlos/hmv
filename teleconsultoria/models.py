from django.db import models
from django.utils import timezone

class Solicitante(models.Model):
    txtNome = models.CharField(max_length=100, null="false")
    txtEmail = models.CharField(max_length=100, null="false")
    txtTelefone = models.CharField(max_length=11, null="false")  # telefone com DD e 9 digitos
    txtCPF = models.CharField(max_length=11, null="false")

    def __str__(self):
        return self.txtNome + ' - ' + self.txtCPF

class Teleconsultor(models.Model):
    txtNome = models.CharField(max_length=100, null="false")
    txtEmail = models.CharField(max_length=100, null="false")
    txtCRM = models.CharField(max_length=20, null="false")
    dtFormatura = models.DateTimeField(default=timezone.now, null="false")

class Solicitacao(models.Model):
    teleconsultor = models.ForeignKey(Teleconsultor, null="false")
    solicitante = models.ForeignKey(Solicitante, null="false")
    txtDescricao= models.CharField(max_length=500, null="false")


