from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Projects(models.Model):
    project_name = models.CharField(max_length=100)
    project_client_name = models.CharField(max_length=100)
    project_client_number = models.CharField(max_length=20)
    project_client_address = models.CharField(max_length=100)
    def __str__(self):
        return self.project_name
    


class Employees(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employees_photo = models.ImageField(upload_to='employees_photo')
    employees_number = models.CharField(max_length=20)
    employees_job = models.CharField(max_length=100)
    employees_address = models.CharField(max_length=20)
    employee_email= models.EmailField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    


class TimeSheet(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
        ('Approved', 'Aprooved'),
    )
    LOCATION = (
        ('Office', 'Office'),
        ('Work From Home', 'Work From Home'),

    )
    TYPE = (
        ('New', 'New'),
        ('Rework', 'Rework'),
        ('Edit', 'Edit'),
    )
    TYPE2 = (
        ('Other', 'Other'),
        ('Poster', 'Poster'),
        ('Video', 'Video'),
        ('Branding', 'Branding'),
        ('Brochure', 'Brochure'),
        ('Packaging', 'Packaging'),
        ('Developing', 'Developing'),

    )
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100, choices=LOCATION)
    type = models.CharField(max_length=100, choices=TYPE)
    type2 = models.CharField(max_length=100, choices=TYPE2)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)   
    status = models.CharField(max_length=100, choices=STATUS, default='Pending')
    description = models.CharField(max_length=500)


    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.date}"