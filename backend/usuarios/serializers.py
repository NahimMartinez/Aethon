"""
Serializadores de Usuarios.
Transforman los modelos de base de datos (User, Atleta, Categoria)
en formato JSON para que el frontend los pueda consumir, y validan los datos entrantes.
"""
from rest_framework import serializers
from .models import Usuario

class RegistroUsuarioSerializer(serializers.ModelSerializer):

    # Le digo que la contraseña es solo de escritura.
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        # Lista de campos que se esperan recibir.
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'dni', 'imagen']

    # Sobreescribo el método de guardado.
    def create(self, validated_data):

        # Uso create_user el cual ya me encripta la contraseña.
        usuario_nuevo = Usuario.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            dni=validated_data['dni'],
            imagen=validated_data['imagen']
        )

        return usuario_nuevo
    

class UsuarioSerializer(serializers.ModelSerializer):
    """
    Solo para mostrar usuarios
    """

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'dni', 'imagen']