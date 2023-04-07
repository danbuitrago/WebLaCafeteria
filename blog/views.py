from django.shortcuts import render, get_object_or_404      #se agrega get object en caso que la categoria no exista
from .models import Post, Category             #se importa desde models de esta carpeta el modelo Post

# Create your views here.
def blog(request):
    posts=Post.objects.all()                                     #se agregan todos los objetos creados en BD desde blog
    return render(request, 'blog/blog.html',{'posts':posts})          #agregamos el diccionario de contexto 


#creamos la vista de categorias
def category(request, category_id):
    category=get_object_or_404(Category,id=category_id)
    #posts=Post.objects.filter(categories=category)          #filtro para mostrar las categorias que si existen cuando se pasa el get_object_404 lo quitamos luego para hacer la revisión inversa con ...
    return render(request, 'blog/category.html', {'category':category})     #,'posts':posts})     #se adiciona el diccionario de contexto posts 