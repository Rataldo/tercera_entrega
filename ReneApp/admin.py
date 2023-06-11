from django.contrib import admin
from .models import Curso, Estudiante, Profesor
# Register your models here.

admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Curso)