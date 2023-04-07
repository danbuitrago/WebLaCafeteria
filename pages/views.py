from django.shortcuts import render, get_object_or_404    #agregamos la libreria de 404
from .models import Page                                    #importamos el modelo Page de esta misma app

#creamos la vista de categorias
def page(request, page_id, page_slug):
    page=get_object_or_404(Page,id=page_id)
    return render(request, 'pages/sample.html', {'page':page})     #,'page':page})     #se adiciona el diccionario de contexto page