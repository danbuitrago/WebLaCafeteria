from django.urls import path
from . import views             #del directorio actual importamos las vistas

urlpatterns = [
    #PATH CORE

    path('', views.services, name='services'),

]