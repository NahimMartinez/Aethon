from django.urls import path
from .views import (
    RegistroCategoriaListCreateView,
    RegistroCoachRolListCreateView,
    RegistroCoachCategoriaListCreateView
)

urlpatterns = [
    # Ruta: /api/institucion/categorias/
    path('categorias/', RegistroCategoriaListCreateView.as_view(), name='lista-categorias'),
    
    # Ruta: /api/institucion/roles/
    path('roles/', RegistroCoachRolListCreateView.as_view(), name='lista-roles'),
    
    # Ruta: /api/institucion/asignaciones/
    path('asignaciones/', RegistroCoachCategoriaListCreateView.as_view(), name='lista-asignaciones'),
]