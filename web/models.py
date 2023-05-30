from django.db import models

# Create your models here.
class Estudiantes (models.Model):
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    
    class Meta:
        managed=False
        db_table = 'estudiantes'
        
    