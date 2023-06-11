from django.shortcuts import render
from ReneApp.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario, BuscarCurso
from .models import *
from django.shortcuts import redirect
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



#Formulario de busqueda de cursos

def buscar_cursos(request):
    if request.method == "POST":
        formulario = BuscarCurso(request.POST)
        if formulario.is_valid():
            termino_busqueda = formulario.cleaned_data['termino_busqueda']
            return resultados_busqueda_cursos(request, termino_busqueda=termino_busqueda)
    else:
        formulario = BuscarCurso()

    return render(request, "ReneApp/buscar_cursos.html", {'formulario': formulario})

def resultados_busqueda_cursos(request, termino_busqueda):
    cursos = Curso.objects.filter(nombre__icontains=termino_busqueda)
    return render(request, "ReneApp/resultados_busqueda_cursos.html", {'cursos': cursos})


