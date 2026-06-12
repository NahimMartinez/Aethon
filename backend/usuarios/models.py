from django.db import models
from PIL import Image
from typing import Any
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    """
    Modelo de Usuario personalizado para Aethon.
    Hereda de AbstractUser para mantener la robustez del sistema de autenticación 
    nativo de Django, extendiéndolo con atributos específicos del negocio.
    """

    dni = models.CharField(max_length=8, blank=False, null=False, unique=True)
    imagen = models.ImageField(upload_to='usuarios/perfiles/', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.username}"
    
    # Sobrescribo el método save para redimensionar las fotos (que todas tengan igual tamaño)
    def save(self, *args: Any, **kwargs: Any) -> None:
        # Guardo el modelo normalmente
        super().save(*args, **kwargs)

        # Verifico si el Atleta realmente tiene una imagen cargada
        if self.imagen:
            # Abro la imagen desde su ruta física
            img = Image.open(self.imagen.path)

            # Verifico si la imagen es muy grande
            if img.height > 600 or img.width > 800:
                tamaño_maximo = (800, 600)
                
                # thumbnail achica la imagen sin deformarla
                img.thumbnail(tamaño_maximo)
                
                # Guardo la imagen achicada, pisando el archivo original
                img.save(self.imagen.path)