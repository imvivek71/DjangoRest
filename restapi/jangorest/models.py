from django.db import models

# Create your models here.

class Employee(models.Model):

    FirstName = models.CharField(max_length=10)
    LastName = models.CharField(max_length=10)
    Age = models.IntegerField()

    def __str__(self):
        return self.FirstName


