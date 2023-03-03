
from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from datetime import datetime

def index(request):
    return render(request,'index.html')


def view_emp(request):
    emps=Employee.objects.all()
    context={'emps':emps}
    return render(request,'view_emp.html',context)


def add_emp(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        Dept=int(request.POST['department'])
        role=int(request.POST['role'])
        salary=request.POST['salary']
        bonus=request.POST['bonus']
        phone=request.POST['phone']
        new_employee=Employee(first_name=first_name,last_name=last_name,Department_id=Dept,Role_id=role,phone=phone,salary=salary,bonus=bonus,hire_date=datetime.now())
        new_employee.save()

        return HttpResponse("employee added successfully")
    
    elif request.method =="GET":
        return render(request,'add_emp.html')
    
    else:
         return HttpResponse("something went wrong")
            
    



def filter_emp(request):

    if request.method =="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        Dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()

        if first_name:
            emps=emps.filter(first_name__icontains = first_name) 
             

        if last_name:
            emps=emps.filter(last_name__icontains = last_name) 

        if Dept:
            emps=emps.filter(Department__name= Dept) 
                 
        if role:
            emps=emps.filter(Role__Name= role)

        context={

            'emps':emps
        }    

        return render(request,'filter_emp.html',context)
                 
    elif request.method=="GET" :
        return render(request,'filter_emp.html')

    else:
        return HttpResponse("An exception occured")
    

def delete_emp(request,emp_id=0):
   
    if emp_id:
        try:
            employee_delt=Employee.objects.get(id=emp_id)
            employee_delt.delete()
            return HttpResponse("employee deleted successfully")
        except:

            return HttpResponse("pls enter a valid id")
        
    emps=Employee.objects.all()
    context={'emps':emps}

    return render(request,'delete_emp.html',context)