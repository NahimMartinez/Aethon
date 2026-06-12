from django.db import models
from PIL import Image
from typing import Any
from datetime import date
from django.conf import settings


class Categoria(models.Model):
    anio = models.IntegerField(unique=True, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.anio}"
    

class Atleta(models.Model):
    nombre = models.CharField(max_length=150, null=False, blank=False)
    apellido = models.CharField(max_length=150, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    imagen = models.ImageField(upload_to='atletas/perfiles/', null=True, blank=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    GENEROS = [
        ('hombre', 'Hombre'),
        ('mujer', 'Mujer'),
    ]
    genero = models.CharField(max_length=7, choices=GENEROS)
    # Clave foránea
    coach = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.apellido} - {self.fecha_nacimiento}"
    
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
    
    @property
    def edad(self) -> int:
        hoy = date.today()
        return hoy.year - self.fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))