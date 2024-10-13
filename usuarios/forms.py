from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class RegistroForm(forms.ModelForm):#Clase para el formulario de registro
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    password_confirmacion = forms.CharField(widget=forms.PasswordInput, label='Confirmar Contraseña')
    rol = forms.ChoiceField(choices=Perfil.ROLES, label='Rol')

    class Meta:#Clase Meta para definir el modelo y los campos del formulario
        model = User
        fields = ['username', 'email', 'password', 'password_confirmacion']#Campos del formulario

    #Método para validar la confirmación de la contraseña, se llama clean_<nombre_campo>
    def clean_password_confirmacion(self):#Método para validar la confirmación de la contraseña
        password = self.cleaned_data.get('password')#Obtenemos la contraseña
        password_confirmacion = self.cleaned_data.get('password_confirmacion')
        if password and password_confirmacion and password != password_confirmacion:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password_confirmacion
