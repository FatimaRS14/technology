from django.shortcuts import render
# from .models import Equipment

def home(request):
    # equipments = Equipment.objects.all()
    return render(request,'home/home.html')


