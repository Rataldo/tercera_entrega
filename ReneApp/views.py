from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request, "ReneApp/index.html")

def cursos(request):
    
    return render(request, "ReneApp/cursos.html")

def estudiantes(request):
    
    return render(request, "ReneApp/estudiantes.html")

def profesores(request):
    
    return render(request, "ReneApp/profesores.html")