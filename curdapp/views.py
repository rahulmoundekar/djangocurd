from django.shortcuts import render, redirect
from curdapp.EmployeeForm import EmployeeForm
from curdapp.models import Employee


# Create your views here.


def employeeList():
    employees = Employee.objects.all()
    return employees


def employee(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EmployeeForm(request.POST)
        empId = request.POST['id']
        if empId.strip():
            id = int(empId)
            employee = Employee.objects.get(id=id)
            form = EmployeeForm(request.POST, instance=employee)
            if form.is_valid():
                form.save()
                return redirect("/")
        else:
            # check whether it's valid:
            if form.is_valid():
                try:
                    form.save()
                    employees = employeeList
                    return redirect('/')
                except:
                    pass
    else:
        form = EmployeeForm()
    employees = employeeList
    return render(request, 'index.html', {'form': form, 'employees': employees})


def getEmployeeById(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST or None, instance=employee)
    employees = employeeList
    return render(request, 'index.html', {'form': form, 'employee': employee, 'employees': employees})


def deleteEmployeeById(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        employee = None
    if employee != None:
        employee.delete()

    employees = employeeList
    form = EmployeeForm()

    return render(request, 'index.html', {'form': form, 'employees': employees})
