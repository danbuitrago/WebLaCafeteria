from django.urls import path
from . import views             #del directorio actual importamos las vistas

urlpatterns = [
    path('<int:page_id>/<slug:page_slug>/',views.page, name='page'),
]