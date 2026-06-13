from django.urls import path
from .views import TipoPruebaListCreateView, RegistroPruebaView

urlpatterns = [
    path('tipos/', TipoPruebaListCreateView.as_view(), name='tipos-prueba'),
    path('registrar/', RegistroPruebaView.as_view(), name='registrar-prueba'),
]