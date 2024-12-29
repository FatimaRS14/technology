from django.urls import path, include
from .views import register_equipment, list_equipment
from . import views

app_name = 'equipment'

urlpatterns = [
    path('register/', views.register_equipment, name="register_equipment"),
    path('list_equipment/', views.list_equipment, name="list_equipment"),
    path('equipment/edit/<str:equipment_id>/', views.edit_equipment, name="edit_equipment"),
    path('delete/<str:equipment_id>/', views.delete_equipment, name='delete_equipment')
]