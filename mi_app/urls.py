
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('inicioSesion/',views.inicioSesion,name='inicioSesion'),
    path('registro/',views.registro,name='registro'),
    path('crearRutina/',views.crearRutina,name='crearRutina'),
    path('iniciarRutina/',views.iniciarRutina,name='iniciarRutina'),
    path('seguirRutina/',views.seguirRutina,name='seguirRutina'),
    path('dashboard/',views.dashboard,name='dashboard'),
]