from django.db import models
from ckeditor.fields import RichTextField   #agregamos ckeditor para enriquecer el editor en el contenido desde admin

# Creamos el modelo de páginas para mostrar en politicas de privacidad, avisos legales y cookies
class Page(models.Model):
    title=models.CharField(verbose_name='Título',max_length=200)
    #content=models.TextField(verbose_name='Contenido')
    content=RichTextField(verbose_name='Contenido')     #SE MODIFICA RICH para gestionar el contenido
    order=models.SmallIntegerField(verbose_name='Orden', default=0)     #se agrega un campo para que el usuario ordene de acuerdo a un número entero 
    created=models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated=models.DateTimeField(verbose_name='Fecha de edición', auto_now=True)

    class Meta:
        verbose_name='página'
        verbose_name_plural='páginas'
        ordering=['order','title']      #se ordena por orden y por titulo, es importante el orden de los campos que recibe, el primero manda.

    def __str__(self):
        return self.title
