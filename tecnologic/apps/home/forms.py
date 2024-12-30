from django import forms
from .models import Assignment

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['id_equipment', 'id_department', 'assignment_date', 'return_date', 'status']
        widgets = {
            'id_equipment': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Selecciona el equipo'}),
            'id_department': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Selecciona el departamento'}),
            'assignment_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'return_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        assigned_equipment = Assignment.objects.filter(status=Assignment.ASSIGNED).values_list('id_equipment_id', flat=True)
        self.fields['id_equipment'].queryset = self.fields['id_equipment'].queryset.exclude(id_equipment__in=assigned_equipment)
