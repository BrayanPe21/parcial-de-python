from django.db import models

# Create your models here.
class Crud(models.Model):
    articulo = models.CharField(max_length=50)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=200)
    cantidad = models.IntegerField()
