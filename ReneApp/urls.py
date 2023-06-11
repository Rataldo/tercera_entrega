from django.urls import path 
from ReneApp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cursos/', views.cursos, name="cursos"),
    path('estudiantes/', views.estudiantes, name="estudiantes" ),
    path('profesores/', views.profesores, name="profesores"),
    path('buscar-cursos/', views.buscar_cursos, name='buscar_cursos'),
    path('resultados-busqueda/<str:termino_busqueda>/', views.resultados_busqueda_cursos, name='resultados_busqueda_cursos'),
]