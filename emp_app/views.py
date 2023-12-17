from django.shortcuts import render, HttpResponse
from .models import Employee
#Role, Department
from datetime import datetime
from django.db.models import Q
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'index.html', context)
    # return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    # print(context)
    return render(request, 'index.html', context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        cisco_id = request.POST['cisco_id']
        status = request.POST['status']
        emps = Employee.objects.all()
        context = {
            'emps': emps
        }
        # salary = int(request.POST['salary'])
        # bonus = int(request.POST['bonus'])
        # phone = int(request.POST['phone'])
        # dept = int(request.POST['dept'])
        # role = int(request.POST['role'])
        # new_emp = Employee(first_name= first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id = dept, role_id = role, hire_date = datetime.now())
        new_emp = Employee(first_name= first_name, last_name=last_name, cisco_id=cisco_id, status=status)
        new_emp.save()
        # return HttpResponse('Employee status added Successfully')
        return render(request, 'index.html', context)
    elif request.method=='GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An Exception Occured! Employee Status Has Not Been Added")


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            emps = Employee.objects.all()
            context = {
                'emps': emps
            }
            # return HttpResponse("Employee Status Removed Successfully")
            return render(request, 'index.html', context)
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html',context)


def filter_emp(request):
    if request.method == 'POST':
        # name = request.POST['name']
        # status = request.POST['status']
        cisco_id = request.POST['cisco_id']
        # role = request.POST['role']
        emps = Employee.objects.all()
        # if name:
        #     emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        # if status:
        #     emps = emps.filter(status__icontains = status)
        if cisco_id:
            emps = emps.filter(cisco_id__icontains = cisco_id)
        # if role:
        #     emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'index.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')

def update(request, emp_id = 0):  
    if emp_id:
        emp_to_be_removed = Employee.objects.get(id=emp_id)
        if request.method == 'POST':
            first_name = emp_to_be_removed.first_name
            last_name = emp_to_be_removed.last_name
            cisco_id = emp_to_be_removed.cisco_id
            status = request.POST['status']
            emps = Employee.objects.all()
            context = {
                'emps': emps
            }
            # salary = int(request.POST['salary'])
            # bonus = int(request.POST['bonus'])
            # phone = int(request.POST['phone'])
            # dept = int(request.POST['dept'])
            # role = int(request.POST['role'])
            # new_emp = Employee(first_name= first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id = dept, role_id = role, hire_date = datetime.now())
            new_emp = Employee(first_name= first_name, last_name=last_name, cisco_id=cisco_id, status=status)
            new_emp.save()
            # return HttpResponse('Employee status added Successfully')
            return render(request, 'add_emp.html', context)
    elif request.method=='GET':
        emps = Employee.objects.all()
        context = {
            'emps': emps
        }
        return render(request, 'remove_emp.html',context)
    else:
        return HttpResponse("An Exception Occured! Employee Status Has Not Been Added")                                

def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        # password = request.POST['password']
        # Check username and password combination if correct
        # user = authenticate(username=username, password=password)
        user = authenticate(username=username)

        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            return render(request, 'index.html')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'login.html')