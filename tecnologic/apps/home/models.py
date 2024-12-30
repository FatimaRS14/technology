from django.db import models
import uuid
from django.utils.timezone import now

class Assignment(models.Model):
    ASSIGNED = 'Asignado'
    RETURNED = 'Devuelto'
    
    STATUS_CHOICES = [
        (ASSIGNED, 'Asignado'),
        (RETURNED, 'Devuelto'),
    ]
    
    id_assignment = models.CharField(max_length=50, primary_key=True, editable=False, unique=True)
    id_equipment = models.ForeignKey('equipment.Equipment', on_delete=models.CASCADE)
    id_department = models.ForeignKey('departments.Department', on_delete=models.CASCADE)
    assignment_date = models.DateTimeField(default=now)
    return_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ASSIGNED)

    def save(self, *args, **kwargs):
        if not self.id_assignment:  
            self.id_assignment = f"Ass{uuid.uuid4().hex[:8]}"  

        Assignment.objects.filter(id_assignment__isnull=True).delete()
        
        super().save(*args, **kwargs)

        is_new = not self.pk
        if not self.id_assignment:
            Assignment.objects.filter(id_assignment__isnull=True).delete()
            self.id_assignment = f"Ass{uuid.uuid4().hex[:8]}"  
        super().save(*args, **kwargs)
        
        if self.status == self.ASSIGNED:
            self.id_equipment.status = 'ASIGNADO'
        elif self.status == self.RETURNED:
            self.id_equipment.status = 'DISPONIBLE'
        self.id_equipment.save()

    class Meta:
        verbose_name = "Asignación"
        ordering = ['-assignment_date'] 

    def __str__(self):
        return f"Asignación de {self.id_equipment} para {self.id_department}"
