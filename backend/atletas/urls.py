from django.urls import path
from .views import RegistroAtletaView

urlpatterns = [
    path('registro/', RegistroAtletaView.as_view(), name='registro-atleta')
]