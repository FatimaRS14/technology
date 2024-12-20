from django.db import models
import uuid

class Department(models.Model):
    id_department = models.CharField(max_length=50, primary_key=True, editable=False, unique=True)
    name = models.CharField(verbose_name="Nombre del Departamento", max_length=100)
    location = models.CharField(verbose_name="Locación", max_length=100)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def save(self, *args, **kwargs):
        if not self.id_department:  
            self.id_department = f"Dep{uuid.uuid4().hex[:8]}"  
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Departamento"
        ordering = ['-created']

    def __str__(self):
        return self.name