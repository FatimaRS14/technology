from django.shortcuts import render, redirect, get_object_or_404
from apps.equipment.models import Equipment
from .models import Assignment  
from .forms import AssignmentForm 
from django.utils.timezone import now
from django.contrib import messages
from apps.departments.models import Department

def home(request):
    total_equipos = Equipment.objects.count()
    equipos_disponibles = Assignment.objects.filter(status ='Devuelto').count()
    equipos_asignados = Assignment.objects.filter(status = 'Asignado').count()

    context = {
        'total_equipos': total_equipos,
        'equipos_disponibles': equipos_disponibles,
        'equipos_asignados': equipos_asignados,
    }
    return render(request,'home/home.html', context)

def register_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.assignment_date = now()
            assignment.save()
            return redirect('home:list_assignments')
    else:
        form = AssignmentForm()

    return render(request, 'home/register_assignment.html', {'form': form})
    

def list_assignments(request):
    active_assignments = Assignment.objects.filter(status=Assignment.ASSIGNED)
    historical_assignments = Assignment.objects.filter(status=Assignment.RETURNED)
    return render(request, 'home/list_assignments.html', {
        'active_assignments': active_assignments,
        'historical_assignments': historical_assignments,
    })

def return_equipment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id_assignment=assignment_id)
    if assignment.status == Assignment.ASSIGNED:
        assignment.status = Assignment.RETURNED
        assignment.return_date = now()
        assignment.save()
        messages.success(request, f'El equipo "{assignment.id_equipment}" ha sido devuelto exitosamente.')
    else:
        messages.error(request, 'El equipo ya ha sido devuelto.')
    return redirect('home:list_assignments')


def recent_activity(request):
    equipment_activity = Equipment.objects.annotate(date=Coalesce('created', 'updated')).values('id_equipment', 'name', 'date')
    department_activity = Department.objects.annotate(date=Coalesce('created', 'updated')).values('id_department', 'name', 'date')
    assignment_activity = Assignment.objects.annotate(date=Coalesce('assignment_date', 'return_date')).values('id_assignment', 'status', 'date')

    combined_activity = list(equipment_activity) + list(department_activity) + list(assignment_activity)
    sorted_activity = sorted(combined_activity, key=lambda x: x['date'], reverse=True)

    context = {
        'activities': sorted_activity[:10]  
    }

    return render(request, 'home/home.html', context)