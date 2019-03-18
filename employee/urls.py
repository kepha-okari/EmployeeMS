from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views


# app_name = 'employee'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/employee/', views.add_employee, name='add_employee'),
    path('edit/employee/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('delete/employee<int:employee_id>/', views.remove_employee, name='remove_employee'),
    path('filter/', views.filter_by_department, name='filter_by_department'),
    path('import/', views.import_csv_data, name='import_csv_data'),
    
]