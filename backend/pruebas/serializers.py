from rest_framework import serializers
from .models import Prueba, TipoPrueba
from typing import Any

class RegistroPruebaSerializer(serializers.ModelSerializer):

    # Hago que el coach no sea obligatorio en la petición que manda el celular
    coach = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Prueba
        fields = ['datos_crudos', 'observaciones', 'atleta', 'tipo_prueba', 'coach']

    def create(self, validated_data: dict[str, Any]) -> Prueba:

        # Extraigo al usuario logueado usando el token de la petición
        coach_asignado = self.context['request'].user

        prueba_nueva = Prueba.objects.create(
            datos_crudos=validated_data['datos_crudos'],
            observaciones=validated_data.get('observaciones', None),            atleta=validated_data['atleta'],
            tipo_prueba=validated_data['tipo_prueba'],
            coach=coach_asignado
        )

        return prueba_nueva
    

class RegistroTipoPruebaSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoPrueba
        fields = ['nombre', 'estrategia', 'unidad_de_medida']

    def create(self, validated_data: dict[str, Any]) -> TipoPrueba:

        tipo_prueba_nueva = TipoPrueba.objects.create(
            nombre=validated_data['nombre'],
            estrategia=validated_data['estrategia'],
            unidad_de_medida=validated_data.get('unidad_de_medida', None),
        )

        return tipo_prueba_nueva