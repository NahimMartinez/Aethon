"""
Serializadores de Usuarios.
Transforman los modelos de base de datos (User, Atleta, Categoria)
en formato JSON para que el frontend los pueda consumir, y validan los datos entrantes.
"""
from rest_framework import serializers