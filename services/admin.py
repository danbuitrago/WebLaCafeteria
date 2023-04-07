from django.contrib import admin
from .models import Service      #importamos el modelo Project del archivo models.py en la misma carpeta services            

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    

admin.site.register(Service,ServiceAdmin)       #registramos el modelo
