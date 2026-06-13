from django.db import models
from atletas.models import Atleta
from django.conf import settings

class TipoPrueba(models.Model):
    nombre = models.CharField(max_length=150, unique=True, blank=False)
    estrategia = models.CharField(max_length=150, unique=True, blank=False)
    unidad_de_medida = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre
    
class Prueba(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    datos_crudos = models.JSONField(null=False, blank=False)
    observaciones = models.TextField(null=True, blank=True)
    puntaje = models.FloatField(null=True, blank=True)
    clima_temperatura = models.FloatField(null=True, blank=True)
    clima_humedad = models.IntegerField(null=True, blank=True)
    clima_condicion = models.CharField(max_length=100, null=True, blank=True)
    # Claves Foráneas    
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE)
    tipo_prueba = models.ForeignKey(TipoPrueba, on_delete=models.RESTRICT)
    coach = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return f"Prueba de {self.atleta.nombre} - {self.tipo_prueba.nombre} ({self.fecha.date()})"
