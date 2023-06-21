from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

# Create your views here.

#Vista de Login request

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "ReneApp/index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "ReneApp/index.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "ReneApp/index.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "Users/login.html", {"form": form})



#Registro de Usuario

def register(request):

    if request.method == 'POST':

        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,"ReneApp/index.html" ,  {"mensaje":"Usuario Creado :)"})

    else:
        # form = UserCreationForm()       
        form = UserRegisterForm()     

    return render(request,"Users/registro.html" ,  {"form":form})


#logout por medio de views (explicado en clase  23)
class Logout(LogoutView): 
    template_name = "Users/logout.html"