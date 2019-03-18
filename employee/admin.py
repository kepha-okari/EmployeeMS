from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'phone',
        'department',
        'employee_id'
 
    )
    list_filter = ('department',)
admin.site.register(Employee, EmployeeAdmin)

