from django.contrib import admin
from .models import Equipment

class EquipmentAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id_equipment', 'name', 'created', 'updated')

admin.site.register(Equipment, EquipmentAdmin)