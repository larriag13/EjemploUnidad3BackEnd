from django.shortcuts import render, redirect, get_object_or_404
from .models import Imagen
from .forms import ImagenForm
from django.contrib.auth.decorators import login_required

def lista_imagenes(request):
    imagenes = Imagen.objects.all().order_by('-fecha_subida')
    return render(request, 'galeria/lista_imagenes.html', {'imagenes': imagenes})

def detalle_imagen(request, pk):
    imagen = get_object_or_404(Imagen, pk=pk)
    return render(request, 'galeria/detalle_imagen.html', {'imagen': imagen})

@login_required
def subir_imagen(request):
    if request.user.perfil.rol in ['editor', 'administrador']:
        if request.method == 'POST':
            form = ImagenForm(request.POST, request.FILES)
            if form.is_valid():
                imagen = form.save(commit=False)
                imagen.autor = request.user
                imagen.save()
                return redirect('galeria:detalle_imagen', pk=imagen.pk)
        else:
            form = ImagenForm()
        return render(request, 'galeria/subir_imagen.html', {'form': form})
    else:
        return redirect('galeria:lista_imagenes')

