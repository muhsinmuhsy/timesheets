from django.urls import path
from . import views

urlpatterns=[
   

    # ---------------- index -------------------------#

    path('', views.index, name='index'),

    # ------------------------------- Project ------------------------------------------------- #

    path('projects/', views.project_list, name='project-list'),
    path('projects/create/', views.project_create, name='project-create'),
    path('projects/update/<int:pk>/', views.project_update, name='project-update'),
    path('projects/delete/<int:pk>/', views.project_delete, name='project-delete'),

    # --------------------------------- Employees ----------------------------------------------- #
    path('employees/', views.employee_list, name='employee-list'),
    path('employee/<int:employee_id>/', views.employee_details, name='employee_details'),
    path('employees/create/', views.employee_create, name='employee-create'),
    path('employees/update/<int:pk>/', views.employee_update, name='employee-update'),
    path('employees/delete/<int:pk>/', views.employee_delete, name='employee-delete'),


    path('timesheet/create/', views.create_timesheet, name='create-timesheet'),
    path('timesheet/list/', views.timesheet_list, name='timesheet-list'),
    path('timesheet/<int:pk>/update/', views.update_timesheet_status, name='update-timesheet-status'),
    path('timesheet_delete/<int:pk>/', views.delete_timesheet, name= 'delete-timesheet'),

    # --------------------------------- Profile -----------------------------------------#

    path('profile/', views.profile, name='profile'),
    path('profileedit/<int:pk>/', views.profileedit, name='profileedit'),
    path('profilephoto/<int:pk>/', views.profilephoto, name='profilephoto'),
]