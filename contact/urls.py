from django.urls import path
from . import views             #del directorio actual importamos las vistas

urlpatterns = [
    path('',views.contact, name='contact'),
]