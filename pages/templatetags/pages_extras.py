from django import template
from pages.models import Page

#transformamos una función normal en un tag simple y lo registramos en la libreria de templates
register=template.Library()
@register.simple_tag        #decorador

def get_page_list():
    pages=Page.objects.all()
    return pages
