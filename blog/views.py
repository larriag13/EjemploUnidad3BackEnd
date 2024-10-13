from django.shortcuts import render, redirect, get_object_or_404
from .models import Articulo
from .forms import ArticuloForm
from django.contrib.auth.decorators import login_required

def lista_articulos(request):
    articulos = Articulo.objects.all().order_by('-fecha_publicacion')
    return render(request, 'blog/lista_articulos.html', {'articulos': articulos})

def detalle_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    return render(request, 'blog/detalle_articulo.html', {'articulo': articulo})

@login_required
def crear_articulo(request):
    if request.user.perfil.rol in ['editor', 'administrador']:
        if request.method == 'POST':
            form = ArticuloForm(request.POST)
            if form.is_valid():
                articulo = form.save(commit=False)
                articulo.autor = request.user
                articulo.save()
                return redirect('blog:detalle_articulo', pk=articulo.pk)
        else:
            form = ArticuloForm()
        return render(request, 'blog/crear_articulo.html', {'form': form})
    else:
        return redirect('blog:lista_articulos')

@login_required
def editar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.user == articulo.autor or request.user.perfil.rol == 'administrador':
        if request.method == 'POST':
            form = ArticuloForm(request.POST, instance=articulo)
            if form.is_valid():
                form.save()
                return redirect('blog:detalle_articulo', pk=articulo.pk)
        else:
            form = ArticuloForm(instance=articulo)
        return render(request, 'blog/editar_articulo.html', {'form': form})
    else:
        return redirect('blog:lista_articulos')