from django.urls import path
from . import views             #del directorio actual importamos las vistas

urlpatterns = [

 path('', views.blog, name='blog'),     #path pegado desde urls.py de la app core
 path('category/<int:category_id>/', views.category, name='category'),            #agregamos el path de category con un ID

]