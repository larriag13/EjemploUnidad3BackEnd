from django.db.models.signals import post_save#Importamos la señal post_save, que se ejecuta después de guardar un objeto
from django.dispatch import receiver#Importamos el decorador receiver, que se utiliza para registrar una señal
from django.contrib.auth.models import User#Importamos el modelo User de la app auth
from .models import Perfil#Importamos el modelo Perfil de la app usuarios

#Función para crear un perfil de usuario al crear un usuario
@receiver(post_save, sender=User)
#El decorador receiver registra la señal post_save del modelo User
def crear_perfil_usuario(sender, instance, created, **kwargs):#Función que recibe la señal post_save
    if created:#Si se ha creado un usuario
        Perfil.objects.create(user=instance)#Creamos un perfil de usuario con el usuario creado

#Función para guardar el perfil de usuario al guardar un usuario
@receiver(post_save, sender=User)#
def guardar_perfil_usuario(sender, instance, **kwargs):#Función que recibe la señal post_save
    instance.perfil.save()#Guardamos el perfil del usuario