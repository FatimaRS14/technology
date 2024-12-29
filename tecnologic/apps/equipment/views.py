from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import EquipmentRegisterForm
from .models import Equipment
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def register_equipment(request):
    if request.method == 'POST':
        form = EquipmentRegisterForm(request.POST)
        if form.is_valid():
            equipment = form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Equipo registrado exitosamente.',
                    'redirect_url': reverse('equipment:list_equipment')  
                })
            else:
                return redirect('equipment:list_equipment')  
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'message': 'Error al registrar el equipo. Verifica los datos ingresados.'
                })
    else:
        form = EquipmentRegisterForm()

    return render(request, 'equipment/register_equipment.html', {'form': form})

def list_equipment(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment/list_equipment.html', {'equipments': equipments})

def edit_equipment(request, equipment_id=None):
    is_edit = equipment_id is not None
    equipment = None

    if is_edit:
        equipment = get_object_or_404(Equipment, id_equipment=equipment_id)

    if request.method == 'POST':
        form = EquipmentRegisterForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Equipo actualizado correctamente.' if is_edit else 'Equipo registrado correctamente.',
                    'redirect_url': reverse('equipment:list_equipment')  
                })
            else:
                return redirect('equipment:list_equipment')  
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'message': 'Hubo un error al guardar el equipo. Verifica los datos ingresados.'
                })
            else:
                return render(request, 'equipment/register_equipment.html', {
                    'form': form,
                    'is_edit': is_edit,
                    'equipment': equipment,
                    'error_message': 'Hubo un error al guardar el equipo. Verifica los datos ingresados.'
                })
    else:
        form = EquipmentRegisterForm(instance=equipment)

    return render(request, 'equipment/register_equipment.html', {
        'form': form,
        'is_edit': is_edit,
        'equipment': equipment
    })

@csrf_exempt  
def delete_equipment(request, equipment_id):
    if request.method == 'POST':
        try:
            equipment = Equipment.objects.get(id_equipment=equipment_id)
            equipment.delete()
            return JsonResponse({'success': True, 'message': 'Equipo eliminado correctamente.'})
        except Equipment.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Equipo no encontrado'}, status=404)
    return JsonResponse({'success': False, 'message': 'Funcion no permitida'}, status=405)
