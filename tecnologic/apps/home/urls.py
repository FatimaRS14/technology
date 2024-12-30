from django.urls import path
from .import views

app_name = 'home'
urlpatterns = [
     path('', views.home, name='home'),
     path('register/', views.register_assignment, name='register_assignment'),
     path('list/', views.list_assignments, name='list_assignments'),
     path('return/<str:assignment_id>/', views.return_equipment, name='return_equipment'),
]