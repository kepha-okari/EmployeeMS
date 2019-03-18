from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import datetime
from datetime import timedelta

class Employee(models.Model):

    DEPARTMENT_CHOICES = ( 
        ('O', 'Operations'),
        ('F', 'Finance'),
        ('H', 'HR'),
        ('M', 'Marketing'),
        ('R', 'R & D'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True) #optional
    department = models.CharField(max_length=1, choices=DEPARTMENT_CHOICES, default='O')
    employee_id = models.CharField(max_length=50, unique=True, blank=True, null=True)


    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    @classmethod
    def get_employees(cls):
        '''
        Method that gets all employee from the database
        Returns:
            emlpoyees : list of iemployee objects from the database
        '''
        employees = cls.objects.all()
        return employees

    # @classmethod
    def delete_employee(self):

        # employee = cls.objects.get(id=employee_id)

        self.delete()