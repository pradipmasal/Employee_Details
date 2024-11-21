from django.shortcuts import render,get_object_or_404

from employee.models import Employee
# from django.core.files.storage import FileSystemStorage

# Create your views here.
def new_employee(request):
    if(request.method=="POST"):
        f_name = request.POST['firstname']
        l_name = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phonenumber']
        desg = request.POST['designation']
        aboutme = request.POST['aboutme']
        photo = request.FILES['photo']

        instance = Employee(first_name = f_name, last_name=l_name, email_id = email, phone_number = phone, designation = desg, about_me = aboutme, photo = photo)
        instance.save()
    return render(request,'new_employee.html')

def employees(request):
    emp = Employee.objects.all()
    context={
        'emp':emp,
    }
    return render(request,'employees.html',context)

def employee_details(request,pk):
    employee = get_object_or_404(Employee,pk=pk)
    context={
        'emp':employee,
    }
    return render(request,'employee_details.html',context)