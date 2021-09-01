from rest_framework import serializers

from . models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

'''

class EmployeeSerializer(serializers.ModelSerializer):
    emp_code = serializers.CharField(max_length=200, null=False, blank=False, unique=True)
    department = serializers.CharField(ax_length=200, null=False, blank=False)
    score = serializers.IntegerField()
    date_created = serializers.DateField()

'''
