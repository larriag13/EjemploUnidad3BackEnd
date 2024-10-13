from django.apps import AppConfig


class UsuariosConfig(AppConfig):#Configuración de la app usuarios
    #default_auto_field = 'django.db.models.BigAutoField'#Campo para la clave primaria, por defecto
    name = 'usuarios'#Nombre de la app, en este caso usuarios

    def ready(self):
        import usuarios.signals #Importamos el archivo signals.py
