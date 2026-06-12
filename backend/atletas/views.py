from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import RegistroAtletaSerializer
from .models import Atleta

class RegistroAtletaView(generics.CreateAPIView):
    # El Queryset para decirle a DRF en que conjunto de objetos debe operar.
    queryset = Atleta.objects.all()

    # Creo el Serializer para que revise que los datos sean correctos.
    serializer_class = RegistroAtletaSerializer

    #
    permission_classes = [IsAuthenticated]

