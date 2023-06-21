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


urlpatterns += [  path('class-list/', views.CursoList.as_view(), name="List"),
    path('class-detail/<pk>/', views.CursoDetail.as_view(), name="Detail"),
    path('class-create/', views.CursoCreate.as_view(), name="Create"),
    path('class-update/<pk>/', views.CursoUpdate.as_view(), name="Update"),
    path('class-delete/<pk>/', views.CursoDelete.as_view(), name="Delete"),
    
]