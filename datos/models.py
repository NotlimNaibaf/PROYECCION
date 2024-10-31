from django.db import models

from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    ROLES = (
        ('admin', 'Administrador'),
        ('normal', 'Usuario Normal'),
    )

    rol = models.CharField(max_length=7, choices=ROLES, default='normal')


class Datos(models.Model):
    galpon = models.CharField(max_length=2)
    genetica = models.CharField(max_length=4)
    sexo = models.CharField(max_length=6)
    clima = models.CharField(max_length=10)
    edad = models.PositiveIntegerField()
    peso0 = models.PositiveIntegerField()
    peso7 = models.PositiveIntegerField()
    peso14 = models.PositiveIntegerField()
    peso21 = models.PositiveIntegerField()
    peso28 = models.PositiveIntegerField()
    peso35 = models.PositiveIntegerField()
    pesomonit = models.PositiveIntegerField()

    lote = models.ManyToManyField(Usuario, related_name='datos_pesos', blank=True)

    def __str__(self):
        return self.galpon