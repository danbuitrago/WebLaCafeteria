from django.apps import AppConfig

#configuraciòn de la app pages a otro nombre gestor de páginas
class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
    verbose_name='Gestor de páginas'
