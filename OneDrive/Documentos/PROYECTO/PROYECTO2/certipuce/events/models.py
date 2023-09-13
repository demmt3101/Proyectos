from django.db import models


# Create your models here.
class Events(models.Model):
    id_event = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    fecha = models.DateField()
    hora = models.DateTimeField()
    lugar = models.CharField(max_length=30)

    def __str__(self) -> str:
        return super().__str__()


class Person(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    nombres = models.CharField(max_length=35)
    apellidos = models.CharField(max_length=35)
    email = models.CharField(max_length=100)
