from django import forms
from .models import Equipment

class EquipmentRegisterForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'type_equipment', 'brand', 'model', 'serial_number', 'status', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'type_equipment': forms.Select(attrs={'class': 'form-select', 'id': 'type_equipment'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'id': 'brand'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'id': 'model'}),
            'serial_number': forms.NumberInput(attrs={'class': 'form-control', 'id': 'serial_number'}),
            'status': forms.Select(attrs={'class': 'form-select', 'id': 'status'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'id': 'location'}),
        }