from django import forms
from .models import Department

class DepartmentRegisterForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'location']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del departamento',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la ubicación del departamento',
            }),
        }
        labels = {
            'name': 'Nombre del Departamento',
            'location': 'Ubicación',
        }