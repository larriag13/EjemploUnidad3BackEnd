from django.db import models
from django.contrib.auth.models import User #Importamos el modelo User de la app auth
# Create your models here.

class Perfil(models.Model):
    ROLES = (#Definimos una tupla con los roles que puede tener un usuario
        ('administrador','Administrador'),
        ('editor','Editor'),
        ('usuario','Usuario'),
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)#Relación uno a uno con la tabla User
    rol=models.CharField(max_length=20,choices=ROLES,default='usuario')#Campo para el rol del usuario
    foto=models.ImageField(upload_to='fotos_perfil',null=True,blank=True)#Campo para la foto del usuario

    def __str__(self):
        return f"{self.user.username} - {self.rol}"