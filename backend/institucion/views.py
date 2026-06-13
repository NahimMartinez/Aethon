from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Categoria, CoachCategoria, CoachRol
from .serializers import RegistroCategoriaSerializer, RegistroCoachRolSerializer, RegistroCoachCategoriaSerializer

class RegistroCategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = RegistroCategoriaSerializer
    permission_classes = [IsAuthenticated]

class RegistroCoachRolListCreateView(generics.ListCreateAPIView):
    queryset = CoachRol.objects.all()
    serializer_class = RegistroCoachRolSerializer
    permission_classes = [IsAuthenticated]

class RegistroCoachCategoriaListCreateView(generics.ListCreateAPIView):
    queryset = CoachCategoria.objects.all()
    serializer_class = RegistroCoachCategoriaSerializer
    permission_classes = [IsAuthenticated]

