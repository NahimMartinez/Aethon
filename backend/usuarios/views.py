from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Usuario
from .serializers import RegistroUsuarioSerializer


class RegistroUsuarioView(generics.CreateAPIView):
    # El Queryset para decirle a DRF en que conjunto de objetos debe operar.
    queryset = Usuario.objects.all()

    # Creo el Serializer para que revise que los datos sean correctos.
    serializer_class = RegistroUsuarioSerializer

    #
    permission_classes = [AllowAny]
