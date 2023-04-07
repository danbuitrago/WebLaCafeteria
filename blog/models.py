from django.db import models
from django.utils.timezone import now           #AGREGAMOS LA LIBRERIA TIMEZONE PARA ADICIONAR LA FECHA DE HOY
from django.contrib.auth.models import User     #IMPORTAMOS EL MODELO USER para gestionar los usuarios y sus autenticaciones

# CREAMOS EL MODELO CATEGORIA QUE INCLUYE VARIAS ENTRADAS
class Category (models.Model):
    name=models.CharField(max_length=50, verbose_name='Nombre de categoría')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name="categoría"
        verbose_name_plural="categorías"
        ordering=['-created']

    def __str__(self):
        return self.name
    
# CREAMOS EL MODELO POST PARA LAS ENTRADAS
class Post(models.Model):
    title=models.CharField(max_length=100,verbose_name='Título')
    content=models.TextField(verbose_name='Contenido')
    published=models.DateTimeField(verbose_name='Fecha de publicación',default=now)
    image=models.ImageField(null=True,blank=True,verbose_name='Imagen',upload_to='blog')

    author=models.ForeignKey(User,verbose_name='Autor',on_delete=models.CASCADE)            #AUTOR LLAVE FORANEA DEL MODELO USER PARA DJANGO GESTIONAR USUARIOS
    categories=models.ManyToManyField(Category,verbose_name='Categoría',related_name='get_posts')                       #CATEGORIA PARA GESTIONAR UNA CATEGORIA CON VARIAS ENTRADAS
    
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name='entrada'
        verbose_name_plural='entradas'
        ordering=['-created']

    def __str__(self):
        return self.title


