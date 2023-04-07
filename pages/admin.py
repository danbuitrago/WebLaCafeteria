from django.contrib import admin
from .models import Page                #importamos Page de model de esta app

# configuracion del admin de esta app para mostrar campos de solo lectura created updated
class PageAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('title', 'order')             #se agrega al admin de django una lista ordenada por titulo y orden para que el usuario lo edite

admin.site.register(Page,PageAdmin)     #registrar la app page y pageadmin
