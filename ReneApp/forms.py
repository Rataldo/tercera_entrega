from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
    
    
class EstudianteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

    
class ProfesorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    
    
    
class BuscarCurso(forms.Form):
    termino_busqueda = forms.CharField(label='Ingrese el nombre del curso')
