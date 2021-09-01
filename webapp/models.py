from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_code = models.CharField(max_length=200, null=False, blank=False, unique=True)
    department = models.CharField(max_length=200, null=False, blank=False)
    score = models.IntegerField()
    date_created = models.DateField()

# admin id try3
# password try3
    