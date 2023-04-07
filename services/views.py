from django.shortcuts import render
from .models import Service             #SE AGREGA EL MODELO SERVICE DESDE MODELS
# Create your views here.

def services(request):
    services=Service.objects.all()                      #AGREGA TODOS LOS OBJETOS DE MODELO
    return render(request, "services/services.html", {'services':services})     #DICCIONARIO DE CONTEXTO
