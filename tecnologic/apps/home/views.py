from django.shortcuts import render, redirect, get_object_or_404
from apps.equipment.models import Equipment
from .models import Assignment  
from .forms import AssignmentForm 
from django.utils.timezone import now
from django.contrib import messages
from apps.departments.models import Department
from django.db.models.functions import Coalesce
from django.db.models import Count

def home(request):
    total_equipos = Equipment.objects.count()
    equipos_disponibles = Assignment.objects.filter(status ='Devuelto').count()
    equipos_asignados = Assignment.objects.filter(status = 'Asignado').count()
    equipos_mas_asignados = Equipment.objects.annotate(assignments_count=Count('assignment')).order_by('-assignments_count')[:5]
    
    chart_data = [{
        'name': equipo.name,
        'value': equipo.assignments_count
    } for equipo in equipos_mas_asignados]

    context = {
        'total_equipos': total_equipos,
        'equipos_disponibles': equipos_disponibles,
        'equipos_asignados': equipos_asignados,
        'chart_data': chart_data,
    }
    return render(request,'home/home.html', context)

def register_assignment(request):
    records_without_id = Assignment.objects.filter(id_assignment__isnull=True)
    if records_without_id.exists():
        records_without_id.delete()
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




