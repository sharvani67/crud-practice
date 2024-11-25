from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('operations/', login_required(views.operations), name='operations'),
    path('student/', login_required(views.student), name='student'),
    path('task/',login_required(views.task), name='task'),
    path('employee/', login_required(views.employee), name='employee'),
    path('student_list/', login_required(views.student_list), name='student_list'),
    path('employee_list/', login_required(views.employee_list), name='employee_list'),
    path('task_list/', login_required(views.task_list), name='task_list'),
    path('operation_list/', login_required(views.operation_list), name='operation_list'),
    path('delete_employee/<int:id>/', views.delete_employee, name='delete_employee'),  # Updated
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),   
    path('delete_task/<int:id>/', views.delete_task, name='delete_task'),  
    path('delete_contacts/<int:id>/', views.delete_contacts, name='delete_contacts'), 
    path('update_contacts/<int:id>/', views.update_contacts, name='update_contacts'), 
    path('update_task/<int:id>/', views.update_task, name='update_task'), 
    path('update_employee/<int:id>/', views.update_employee, name='update_employee'), 
    path('update_students/<int:id>/', views.update_students, name='update_students'),   
    path('index/', views.index, name='index'),
    path('view_contact/<int:id>/', views.view_contact, name='view_contact'),
    path('view_employee/<int:id>/', views.view_employee, name='view_employee'),
    path('view_student/<int:id>/', views.view_student, name='view_student'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('register/', views.register, name='register'),
    

]

