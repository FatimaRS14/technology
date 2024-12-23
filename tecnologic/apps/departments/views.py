from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import DepartmentRegisterForm
from .models import Department
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def register_department(request):
    form = DepartmentRegisterForm()
    if request.method == 'POST':
        form = DepartmentRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departments:list_department')  
    else:
        form = DepartmentRegisterForm()

    return render(request, 'departments/register_department.html', {'form': form})

def list_department(request):
    departments = Department.objects.all()
    return render(request, 'departments/list_department.html', {'departments' : departments})


def edit_department(request, department_id=None):
    is_edit = department_id is not None
    department = None
    
    if is_edit:
        department = get_object_or_404(Department, id_department=department_id)
    
    if request.method == 'POST':
        form = DepartmentRegisterForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            response_data = {
                'success': True,
                'message': 'Departamento actualizado correctamente.' if is_edit else 'Departamento creado correctamente.',
                'redirect_url': reverse('departments:list_department') 
            }
            return JsonResponse(response_data)
        else:
            response_data = {
                'success': False,
                'message': 'Hubo un error al guardar el departamento.'
            }
            return JsonResponse(response_data)
    
    else:
        form = DepartmentRegisterForm(instance=department)
    
    return render(request, 'departments/register_department.html', {'form': form, 'is_edit': is_edit, 'department': department})


@csrf_exempt
def delete_department(request, department_id):
    if request.method == 'POST':
        try:
            department = Department.objects.get(id_department=department_id)
            department.delete()
            return JsonResponse({'success': True, 'message': 'Departamento eliminado correctamente.'})
        except Department.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Departamento no encontrado.'}, status=404)
    return JsonResponse({'success': False, 'message': 'Método no permitido.'}, status=405)
