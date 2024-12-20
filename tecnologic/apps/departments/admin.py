from django.contrib import admin
from .models import Department

class DepartmentAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id_department', 'name', 'created', 'updated')

admin.site.register(Department, DepartmentAdmin)
