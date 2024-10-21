from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Perfil

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # No guardamos aún para asignar la contraseña
            user.set_password(form.cleaned_data['password'])  # Encriptamos la contraseña con el método set_password, clean_data para obtener los datos limpios del formulario
            user.save()#Guardamos el usuario
            # Asignamos el rol al perfil
            user.perfil.rol = form.cleaned_data['rol']
            user.perfil.save()
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('usuarios:login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login_view(request):#Vista para el inicio de sesión
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)#Autenticamos al usuario con las credenciales
        if usuario is not None:
            login(request, usuario)#Iniciamos sesión
            return redirect('blog:lista_articulos')#Redireccionamos al inicio de la aplicación si el usuario es autenticado con éxito
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'usuarios/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('usuarios:login')