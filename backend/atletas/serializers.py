from rest_framework import serializers
from .models import Categoria, Atleta
from typing import Any

class RegistroAtletaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Atleta
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'imagen', 'genero', 'coach', 'categoria']

    def create(self, validated_data: dict[str, Any]) -> Atleta:
        
        imagen_recibida = validated_data.get('imagen', None)
        categoria_asignada = validated_data.get('categoria', None)
        coach_asignado = validated_data.get('coach', None)

        if coach_asignado is None:
            coach_asignado = self.context['request'].user

        atleta_nuevo = Atleta.objects.create(
            nombre=validated_data['nombre'],
            apellido=validated_data['apellido'],
            fecha_nacimiento=validated_data['fecha_nacimiento'],
            imagen=imagen_recibida,
            genero=validated_data['genero'],
            categoria=categoria_asignada,
            coach=coach_asignado
        )

        return atleta_nuevo