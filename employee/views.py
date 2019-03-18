from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from employee.models import Employee
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib import messages
import csv



def index(request):
    employees_list = Employee.get_employees()

    page = request.GET.get('page', 1)

    paginator = Paginator(employees_list, 10)
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {"employees":employees})



def filter_by_department(request, department):
    employees_list = Employee.object.filter(department=department)

    page = request.GET.get('page', 1)

    paginator = Paginator(employees_list, 10)
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {"employees":employees})


def remove_employee(request, employee_id):
    Employee.objects.filter(id=employee_id).delete()
    messages.success(request, 'The record has been deleted successfully')
    return redirect(index)


def add_employee(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        department = request.POST['department']
        employee_number = request.POST.get('staff')

        form, created = Employee.objects.get_or_create(first_name=first_name,
                                                    last_name=last_name,
                                                    email=email,
                                                    phone=phone,
                                                    department=department,
                                                    employee_id=employee_number
                                                    )
        form.save()
        return redirect(index)
    return render(request, 'add_employee.html')
    pass


def edit_employee(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        department = request.POST['department']

        employee.first_name = first_name
        employee.last_name = last_name
        employee.phone = phone
        employee. department = department
        employee.save()
       
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'edit_employee.html', {"employee":employee})

def import_csv_data(request):
    """
    Import csv data and save it to database
    """

    csv.register_dialect('myDialect',
    quoting=csv.QUOTE_ALL,
    skipinitialspace=True)

    csv_file = request.POST['csv_file']

    # read the line to edit
    with open(csv_file, 'r') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        size = len(lines)

        records_added = 0

        # to exclude the headings, dont read the first line
        for i in range(1, size):
            # read data in each row
            for line in lines:
                record = Employee(first_name = line[0],
                                last_name = line[1],
                                email = line[2],
                                phone = line[3],
                                department = line[4],
                                employee_id = line[5]
                                )
                record.save()
                records_added += 1 #number of records saved

    readFile.close()

def export_data_to_csv_file(request):
    employees = Employee.objects.all()

    records_added = len(employees)

    with open('media/employees.csv', 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        title = [head.upper() for head in ['Firstname', 'Lastname', 'Email', 'Phone', 'Department', 'EmployeeId' ]]
        # write headers first
        filewriter.writerow(title)
        #save records on csv file 
        for employee in employees:
            filewriter.writerow([employee.first_name, employee.last_name, employee.email, employee.phone, employee.department, employee.employee_id])

    csvFile.close()

