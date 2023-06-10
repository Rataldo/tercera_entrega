from django.urls import path 
from ReneApp import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('cursos/', views.cursos, name="cursos"),
    path('estudiantes/', views.estudiantes, name="estudiantes" ),
    path('profesores/', views.profesores, name="profesores"),
]