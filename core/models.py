from django.db import models
from django.utils import timezone

class Registro(models.Model):
    ESTADO_CHOICES = [
        ("al dia", "Al día"),
        ("moroso", "Moroso"),
    ]

    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    resultado = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=timezone.now)

    # Borrado lógico (se marca como eliminado en vez de borrar el registro)
    eliminado = models.BooleanField(default=False)
    fecha_eliminacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return f"{self.nombre} - {self.resultado}"

    def soft_delete(self):
        self.eliminado = True
        self.fecha_eliminacion = timezone.now()
        self.save()