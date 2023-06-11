from django.shortcuts import render
from ReneApp.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario
from .models import *
# Create your views here.

def index(request):
    
    return render(request, "ReneApp/index.html")



#formulario de cursos
def cursos(request):
    if request.method == "POST":
        curso_formulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html

        if curso_formulario.is_valid():
            informacion = curso_formulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "ReneApp/index.html")
    else:
        curso_formulario = CursoFormulario()

    return render(request, "ReneApp/cursos.html", {"curso_formulario": curso_formulario})
    



#formulario de estudiantes
def estudiantes(request):
    if request.method == "POST":
        estudiante_formulario = EstudianteFormulario(request.POST) # Aqui me llega la informacion del html

        if estudiante_formulario.is_valid():
            informacion = estudiante_formulario.cleaned_data
            estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            estudiante.save()
            return render(request, "ReneApp/index.html")
    else:
        estudiante_formulario = EstudianteFormulario()

    return render(request, "ReneApp/estudiantes.html", {"estudiante_formulario": estudiante_formulario})



#formulario de profesores
def profesores(request):
    if request.method == "POST":
        profesor_formulario = ProfesorFormulario(request.POST) # Aqui me llega la informacion del html

        if profesor_formulario.is_valid():
            informacion = profesor_formulario.cleaned_data
            profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            profesor.save()
            return render(request, "ReneApp/index.html")
    else:
        profesor_formulario = ProfesorFormulario()

    return render(request, "ReneApp/profesores.html", {"profesor_formulario": profesor_formulario})



