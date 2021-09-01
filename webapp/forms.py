from django import forms
# from .models import Employee
 
class EmpRegister(forms.Form):
    emp_code = forms.CharField()
    department = forms.CharField()
    score = forms.IntegerField()
    date_created = forms.DateField()


    