from django.db import models

# Create your models here.
#CREAMOS LOS CAMPOS QUE VAN EN EL MODELO
class Service(models.Model):
    title=models.CharField(max_length=200, verbose_name='Título')
    subtitle=models.CharField(max_length=200,verbose_name='Subtítulo')
    content=models.TextField(verbose_name='Contenido')
    image=models.ImageField(verbose_name='Imagen',upload_to='services')
    #link=models.URLField(verbose_name='Link',null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True,verbose_name='Fecha de actualización')

    class Meta:
        verbose_name='Servicio'
        verbose_name_plural='Servicios'
        ordering=['-created']

    def __str__(self):
        return self.title
