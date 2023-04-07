from django.shortcuts import render, HttpResponse #AGREGAMOS HTTPRESPONSE EN CASO DE RESPUESTAS HTML
# Create your views here.
#DEFINIMOS LAS VISTAS DE NUESTRA WEB
def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def store(request):
    return render(request, 'core/store.html')

#def sample(request):    se borra para modificarla en views.py de pagesd
 #   return render(request, 'core/sample.html')