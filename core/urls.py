from django.urls import path
from . import views             #del directorio actual importamos las vistas

urlpatterns = [
    #PATH CORE
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    #path cortado y puesto en urls.py de la app services
    path('store/', views.store, name='store'),
    #path('contact/',views.contact, name='contact'),
    #path cortado y puesto en urls.py de la app blog
    #path sample cortado y puesto en urls.py de la app pages
]