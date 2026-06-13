from django.db import models
from django.conf import settings


class Categoria(models.Model):
    anio = models.IntegerField(unique=True, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.anio}"
    
class CoachRol(models.Model):
    nombre = models.CharField(max_length=100, unique=True, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.nombre}"
    
class CoachCategoria(models.Model):
    coach = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    coach_rol = models.ForeignKey(CoachRol, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return f"{self.coach.username} - {self.categoria.anio} ({self.coach_rol.nombre})"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['coach', 'categoria', 'coach_rol'],
                name='unique_coach_categoria_rol'
            )
        ]