from django.contrib import admin
from .models import Category, Post          #agregamos al modelo en esta app Category y Post

# AGREGAMOS EL MODELO DEL ADMIN DE DJANGO PARA CATEGORIAS Y ENTRADAS (POST)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('title','author','published','post_categories')         #ordena en el admin de blog una tabla por titulo, autor y publicacio
    ordering=('title',)                #ordena por fecha
    search_fields=('title', 'content','author__username','categories__name')                    #filtro de busqueda
    date_hierarchy='published'                                                                  #organizar por fecha
    list_filter=('author__username','categories__name',)                        #filtro por autor o categoria aparece en la derecha del admin autor y categorias

#campo creado manualmente para mostrar en la lista del admin cuando las relaciones son de muchos a muchos
    def post_categories(self,obj):                                                      #metodo post_categories para listar, obj cada elemento de la lista
        return ','.join([c.name for c in obj.categories.all().order_by('name')])        #retorna en forma de lista cada categoria y las ordena por nombre separadas por comas
    post_categories.short_description='Categorias'                                      #pone el nombre de la lista categorias 

#REGISTRAR LOS MODELOS CATEGORIA Y POST
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post,PostAdmin)