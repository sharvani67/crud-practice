from django.shortcuts import render
from . models import Contact , Student , Employee, Task
from django.db import transaction
from django.contrib.auth.decorators import login_required
from  . decorators import role_required
# Create your views here.





def operations(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        city = request.POST.get('city')
        pancard = request.POST.get('pancard')
        profile_picture = request.FILES.get('profilepicture')
        print("Received data:", username, mobile, email, city, pancard)
        Contact.objects.create(
            username=username,
            mobile=mobile,
            email=email,
            city=city,
            pancard=pancard,
            profile_picture=profile_picture,
        )
        if request.POST.get('submit') == 'save':
            messages.success(request, 'Contact data has been saved. You can add more Contacts.')
            return render(request, 'operations.html')  # Stay on the same form page

        # If "Submit" button was clicked
        if request.POST.get('submit') == 'submit':
            messages.success(request, 'Contact data has been successfully submitted.')
            return redirect('operation_list')  # Redirect to the contact list page

    # Handle GET requests and render the form
    return render(request, 'operations.html')


    
@role_required('adminstaff')
def student(request):
    if request.method=='POST':
        studentname=request.POST.get('studentname')
        fathername=request.POST.get('fathername')
        mothername=request.POST.get('mothername')
        standard=request.POST.get('standard')
        email=request.POST.get('email')
        marks=request.POST.get('marks')
        profile_picture = request.FILES.get('profilepicture')
        print(studentname,fathername,mothername,standard,email,marks)

        Student.objects.create(
            studentname=studentname,
            fathername=fathername,
            mothername=mothername,
            standard=standard,
            email=email,
            marks=marks,
            profile_picture=profile_picture,
            )
        if request.POST.get('submit') == 'save':
            messages.success(request, 'Student data has been saved. You can add more Students.')
            return render(request, 'student.html')  # Stay on the same form page

        # If "Submit" button was clicked
        if request.POST.get('submit') == 'submit':
            messages.success(request, 'Student data has been successfully submitted.')
            return redirect('student_list')  # Redirect to the student list page

    # Handle GET requests and render the form
    return render(request, 'student.html')
        


    
def task(request):
    if request.method=='POST':
        taskname=request.POST.get('taskname')
        startingdate=request.POST.get('startingdate')
        endingdate=request.POST.get('endingdate')
        status=request.POST.get('status')
        Task.objects.create(
            taskname=taskname,
            startingdate=startingdate,
            endingdate=endingdate,
            status=status,
        )
        if request.POST.get('submit') == 'save':
            messages.success(request, 'Task data has been saved. You can add more Tasks.')
            return render(request, 'task.html')  # Stay on the same form page

        # If "Submit" button was clicked
        if request.POST.get('submit') == 'submit':
            messages.success(request, 'Task data has been successfully submitted.')
            return redirect('task_list')  # Redirect to the task list page

    # Handle GET requests and render the form
    return render(request, 'task.html')


@role_required('adminstaff')
def employee(request):
    if request.method == 'POST':
        employeename = request.POST.get('employeename')
        employeeid = request.POST.get('employeeid')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        profile_picture = request.FILES.get('profilepicture')
        print(employeename, employeeid, email, gender, mobile)  # Debugging
        Employee.objects.create(
            employeename=employeename,
            employeeid=employeeid,
            email=email,
            gender=gender,
            mobile=mobile,
            profile_picture=profile_picture,
        )
        if request.POST.get('submit') == 'save':
            messages.success(request, 'Employee data has been saved. You can add more Employees.')
            return render(request, 'employee.html')  # Stay on the same form page

        # If "Submit" button was clicked
        if request.POST.get('submit') == 'submit':
            messages.success(request, 'Employee data has been successfully submitted.')
            return redirect('employee_list')  # Redirect to the employee list page

    # Handle GET requests and render the form
    return render(request, 'employee.html')


@role_required(['student','adminstaff'])
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})  # Ensure the key matches
    pass


@role_required(['employee','adminstaff'])

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})  # Ensure the key matches

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})  # Ensure the key matches

def operation_list(request):
    contacts = Contact.objects.all()
    return render(request, 'operation_list.html', {'contacts': contacts})  # Ensure the key matches


from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
  # Assuming the model is named 'Employee'

@role_required('adminstaff')
def delete_employee(request, id):
    if request.method == "POST":
        employee = get_object_or_404(Employee, id=id)
        employee.delete()
        messages.success(request, "Employee deleted successfully.")
        # Renumber the serial_number field for all remaining students
        with transaction.atomic():
            employees = Employee.objects.all().order_by('id')
            for index, employee in enumerate(employees, start=1):
                employee.serial_number = index
                employee.save(update_fields=['serial_number'])


        return redirect('employee_list')  # Replace with your list view name
    

@role_required('adminstaff')
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    messages.success(request, 'Student deleted successfully.')

    # Renumber the serial_number field for all remaining students
    with transaction.atomic():
        students = Student.objects.all().order_by('id')
        for index, student in enumerate(students, start=1):
            student.serial_number = index
            student.save(update_fields=['serial_number'])

    return redirect('student_list')
def delete_task(request, id):
    
    task = get_object_or_404(Task, id=id)
    task.delete()
    messages.success(request, "Task deleted successfully.")
        # Renumber the serial_number field for all remaining students
    with transaction.atomic():
        tasks = Task.objects.all().order_by('id')
        for index, task in enumerate(tasks, start=1):
            task.serial_number = index
            task.save(update_fields=['serial_number'])
    return redirect('task_list')  # Replace with your list view name

  # Replace with your list view name

def delete_contacts(request, id):
    if request.method == "POST":
        contact = get_object_or_404(Contact, id=id)
        contact.delete()
        messages.success(request, "Contact deleted successfully.")
        # Renumber the serial_number field for all remaining students
        with transaction.atomic():
            contacts = Contact.objects.all().order_by('id')
            for index, contact in enumerate(contacts, start=1):
                contact.serial_number = index
                contact.save(update_fields=['serial_number'])
        return redirect('operation_list')  # Use the correct name of your list view
    

# Update view
def update_contacts(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        contact.username = request.POST.get("username")
        contact.mobile = request.POST.get("mobile")
        contact.email = request.POST.get("email")
        contact.city = request.POST.get("city")
        contact.pancard = request.POST.get("pancard")
        if 'profilepicture' in request.FILES:
            contact.profile_picture = request.FILES['profilepicture']
        contact.save()
        messages.success(request, "Contact updated successfully!")
        return redirect("operation_list")
    return render(request, "update_contact.html", {"contact": contact})
    

def update_task(request, id):  # Parameter name matches the URL
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.taskname = request.POST.get("taskname")
        task.startingdate = request.POST.get("startingdate")
        task.endingdate = request.POST.get("endingdate")
        task.status = request.POST.get("status")
        
        task.save()
        messages.success(request, "Task updated successfully!")
        return redirect("task_list")

    return render(request, "update_task.html", {"task": task})

@role_required('adminstaff')
def update_students(request, id):  
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.studentname = request.POST.get("studentname")
        student.fathername = request.POST.get("fathername")
        student.mothername = request.POST.get("mothername")
        student.standard = request.POST.get("standard")
        student.email = request.POST.get("email")
        student.marks = request.POST.get("marks")
        
        # Handle profile picture update
        if 'profilepicture' in request.FILES:
            student.profile_picture = request.FILES['profilepicture']
        
        student.save()
        messages.success(request, "Student updated successfully!")
        return redirect("student_list")

    return render(request, "update_student.html", {"student": student})

@role_required('adminstaff')
def update_employee(request, id):  # Parameter name matches the URL
    employee = get_object_or_404(Employee, id=id)
    
    if request.method == "POST":
        employee.employeename = request.POST.get("employeename")
        employee.employeeid = request.POST.get("employeeid")
        employee.email = request.POST.get("email")
        employee.gender = request.POST.get("gender")
        employee.mobile = request.POST.get("mobile")
        
        # Handle profile picture update
        if 'profilepicture' in request.FILES:
            employee.profile_picture = request.FILES['profilepicture']  # Assign the new file
        
        # Save the updated employee object
        employee.save()
        
        messages.success(request, 'Employee data updated successfully.')
        return redirect('employee_list')  # Adjust with your URL name for the list
    
    return render(request, "update_employee.html", {"employee": employee})





@login_required
def index(request):
    return render(request,'index.html')


def view_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    return render(request, 'view_operation.html', {'contact': contact})


@role_required(['employee','adminstaff'])
def view_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'view_employee.html', {'employee': employee})


@role_required(['student','adminstaff'])
def view_student(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'view_student.html', {'student': student})



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile  # Import Profile if you're using it

ROLE_CHOICES = [
    ('employee', 'Employee'),
    ('student', 'Student'),
    ('adminstaff','Adminstaff')
]

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        role = request.POST.get('role')  # Get the role from the form

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")  # Error message
        else:
            # Create the user
            user = User.objects.create_user(username=username, password=password, email=email)
            
            # Assign role to the profile (if using a Profile model)
            Profile.objects.create(user=user, role=role)  # Save the role
            
            messages.success(request, "Registration successful! You can now log in.")  # Success message
            return redirect('login')  # Redirect to the login page

    return render(request, 'register.html', {'role_choices': ROLE_CHOICES})



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(f"User logged in: {user.username}, Role: {user.profile.role}")
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password")
            
    return render(request,'login.html')
