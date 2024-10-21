from django.urls import path
from . import views

app_name = 'galeria'

urlpatterns = [
    path('', views.lista_imagenes, name='lista_imagenes'),
    path('imagen/<int:pk>/', views.detalle_imagen, name='detalle_imagen'),
    path('subir/', views.subir_imagen, name='subir_imagen'),
    path('imagen/<int:pk>/editar/', views.editar_imagen, name='editar_imagen'),
    path('imagen/<int:pk>/eliminar/', views.eliminar_imagen, name='eliminar_imagen'),
]