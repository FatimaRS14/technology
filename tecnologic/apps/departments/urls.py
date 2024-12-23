from django.urls import path, include
from .views import register_department
from . import views

app_name = 'departments'

urlpatterns = [
    path('register/', views.register_department, name='register_department'),
    path('list_department/', views.list_department, name='list_department'),
    path('delete/<str:department_id>/', views.delete_department, name='delete_department'),
    path('departments/edit/<str:department_id>/', views.edit_department, name='edit_department'), 


]

