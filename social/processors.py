#definimos un procesador de contextos para añadir los enlaces de las redes sociales en todos los templates

from .models import Link            #importamos el modelo Link de models de esta misma app

def ctx_dict(request):              #diccionario de contexto segùn requerimiento del cliente
    ctx={}                          #diccionario vacio
    links=Link.objects.all()        #se toman todos los objetos de Link y se pasa a links
    for link in links:
        ctx[link.key]=link.url

    return ctx
