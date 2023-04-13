from django.shortcuts import render

# Create your views here.
#vista pagina index.
def index(request):
    return render(request, 'index.html')
#vista inicio sesion
def inicioSesion(request):
    return render(request, 'inicioSesion.html')

def registro(request):
    return render(request, 'registro.html')

def crearRutina(request):
    return render(request, 'crearRutina.html')

def iniciarRutina(request):
    return render(request, 'iniciarRutina.html')

def seguirRutina(request):
    return render(request, 'seguirRutina.html')

def dashboard(request):
    return render(request, 'dashboard.html')