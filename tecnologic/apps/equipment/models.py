from django.db import models
import uuid

class Equipment(models.Model):
    id_equipment = models.CharField(max_length=50, primary_key=True, editable=False, unique=True)
    name = models.CharField(verbose_name="Nombre del equipo", max_length=100)
    TYPE_EQUIPMENT = [
        ('TIPO1', 'Tipo1'),
        ('TIPO2', 'Tipo2'),
    ]
    type_equipment = models.CharField(verbose_name = "Tipo", max_length=10,
        choices=TYPE_EQUIPMENT)
    brand = models.CharField(verbose_name="Marca", max_length=100)
    model =  models.CharField(verbose_name="Modelo", max_length=100)
    serial_number =  models.IntegerField(verbose_name="Número de serie", unique=True)
    STATUS = [
        ('DISPONIBLE', 'Disponible'),
        ('ASIGNADO', 'Asignado')
    ]
    status = models.CharField(verbose_name = "Estatus", max_length=10,
        choices=STATUS)
    location = models.CharField(verbose_name="Locación", max_length=100)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def save(self, *args, **kwargs):
        if not self.id_equipment:  
            self.id_equipment = f"Eq{uuid.uuid4().hex[:8]}"  
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Equipos"
        ordering = ['-created']

    def __str__(self):
        return self.name