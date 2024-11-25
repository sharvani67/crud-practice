from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[('employee', 'Employee'), ('student', 'Student'),('adminstaff', 'Adminstaff')])

    def __str__(self):
        return f"{self.user.username} - {self.role}"


# Create your models here.
class Contact(models.Model):
    username=models.CharField(max_length=100)
    mobile=models.CharField(max_length=15)
    email = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=15,null=True, blank=True)
    pancard = models.CharField(max_length=20,null=True, blank=True)
    serial_number = models.PositiveIntegerField(default=0)  # New field for display order
    profile_picture = models.ImageField(upload_to='Contact_Profiles/', blank=True, null=True) # Add this line

    def __str__(self):
        return self.username
class Student(models.Model):
    

    studentname = models.CharField(max_length=20, null=True, blank=True)
    fathername = models.CharField(max_length=20, null=True, blank=True)
    mothername = models.CharField(max_length=20, null=True, blank=True)
    standard = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    marks = models.IntegerField()
    serial_number = models.PositiveIntegerField(default=0)  # New field for display order
    profile_picture = models.ImageField(upload_to='Student_Profiles/', blank=True, null=True) # Add this line

    def __str__(self):
        return self.studentname 

class Task(models.Model):
    taskname=models.CharField(max_length=20,)
    startingdate=models.CharField(max_length=20)
    endingdate=models.CharField(max_length=20)
    status=models.CharField(max_length=20,null=True, blank=True)
    serial_number = models.PositiveIntegerField(default=0)  # New field for display order
    
    def __str__(self):
        return self.taskname
class Employee(models.Model):
    employeename=models.CharField(max_length=20,null=True, blank=True)
    employeeid=models.CharField(max_length=20,null=True, blank=True)
    gender=models.CharField(max_length=20,null=True, blank=True)
    mobile=models.CharField(max_length=20,null=True,blank=True)
    email=models.CharField(max_length=100, null=True, blank=True)
    serial_number = models.PositiveIntegerField(default=0)  # New field for display order
    profile_picture = models.ImageField(upload_to='Employee_Profiles/', blank=True, null=True) # Add this line
    def __str__(self):
        return self.employeename


