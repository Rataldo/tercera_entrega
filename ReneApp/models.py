from django.db import models




# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} - camada {self.camada}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    
    def __str__(self):
        return f"Estudiante: {self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    
    def __str__(self):
        return f"Profesor: {self.nombre} {self.apellido}"
    
    
