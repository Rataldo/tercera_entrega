from django.urls import path
from Users import views


urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('registro/', views.register, name="Registro"),
    path('logout/', views.Logout.as_view(), name="Logout") #logout fue agregado a views
]