from rest_framework import serializers
from .models import Categoria, CoachRol, CoachCategoria
from typing import Any

class RegistroCategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ['anio']

    def create(self, validated_data: dict[str, Any]) -> Categoria:

        categoria_nueva = Categoria.objects.create(
            anio=validated_data['anio'],
        )

        return categoria_nueva
    

class RegistroCoachRolSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoachRol
        fields = ['nombre']

    def create(self, validated_data: dict[str, Any]) -> CoachRol:

        coach_rol_nuevo = CoachRol.objects.create(
            nombre=validated_data['nombre'],
        )

        return coach_rol_nuevo
    

class RegistroCoachCategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoachCategoria
        fields = ['coach', 'categoria', 'coach_rol']

    def create(self, validated_data: dict[str, Any]) -> CoachCategoria:

        coach_rol_nuevo = CoachCategoria.objects.create(
            coach=validated_data['coach'],
            categoria=validated_data['categoria'],
            coach_rol=validated_data['coach_rol'],
        )

        return coach_rol_nuevo