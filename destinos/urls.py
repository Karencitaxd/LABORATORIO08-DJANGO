from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.agregar_destino, name='agregar_destino'),
    path('editar/<int:id>/', views.editar_destino, name='editar_destino'),
]