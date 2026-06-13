from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Prueba, TipoPrueba
from .serializers import RegistroPruebaSerializer, RegistroTipoPruebaSerializer

class TipoPruebaListCreateView(generics.ListCreateAPIView):
    """
    GET: Devuelve la lista de todos los tipos de prueba (Para el menú desplegable del Frontend).
    POST: Crea un nuevo tipo de prueba (Solo administradores/staff en el futuro).
    """
    queryset = TipoPrueba.objects.all()
    serializer_class = RegistroTipoPruebaSerializer
    permission_classes = [IsAuthenticated]


class RegistroPruebaView(generics.CreateAPIView):
    """
    POST: Recibe los datos crudos del celular y registra una nueva evaluación.
    """
    queryset = Prueba.objects.all()
    serializer_class = RegistroPruebaSerializer
    permission_classes = [IsAuthenticated]