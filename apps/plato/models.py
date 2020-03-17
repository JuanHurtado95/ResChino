from django.db import models
from django.utils import timezone
# Create your models here.

class ingredientes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50, default='')
    tipo=models.CharField(max_length=50, default='')
    precio=models.CharField(max_length=20, default='')

    def __str__(self):
        return str(self.nombre)

    class Meta:
        db_table = 'plato_ingredientes'


