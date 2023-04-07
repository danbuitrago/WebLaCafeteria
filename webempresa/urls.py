"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include       #AGREGAMOS EL INCLUDE A LA LIBRERIA PARA IMPORTAR DESDE URLS.PY DE CORE
from django.conf import settings            #DE DJANGO.CONF IMPORTAMOS LA CONFIGURACIÓN QUE HICIMOS EN SETTING.PY


urlpatterns = [
    #PATH ADMIN
    path('admin/', admin.site.urls),
    #PATH CORE
    path('', include('core.urls')),            #SE AGREGA EL INCLUDE PARA QUE IMPORTE DESDE CORE LAS URLS
    #PATH SERVICES
    path('services/', include('services.urls')),            #SE AGREGA EL INCLUDE PARA QUE IMPORTE DESDE SERVICES LAS URLS
    #PATH BLOG
    path('blog/', include('blog.urls')),            #SE AGREGA EL INCLUDE PARA QUE IMPORTE DESDE BLOG LAS URLS
    #PATH PAGE
    path('page/', include('pages.urls')),           #SE AGREGA EL INCLUDE PARA QUE IMPORTE DESDE PAGE LAS URLS
    #PATH CONTACT
    path('contact/', include('contact.urls')),           #SE AGREGA EL INCLUDE PARA QUE IMPORTE DESDE PAGE LAS URLS
]

#SI TENEMOS EL DEBUG EN MARCHA ACTIVAMOS LA OPCIÓN DE RECIBIR FICHEROS MEDIA EN LA URL MEDIA DE SETTINGS QUE SE BUSCA EN MEDIA ROOT
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)