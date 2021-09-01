from django.shortcuts import render

# Create your views here.
from rest_framework.renderers import JSONRenderer
from . serializers import EmployeeSerializer
from . models import Employee
from django.http import HttpResponse

#  without query parameter

def EmployeeDetail(request):
    emp = Employee.objects.all()
    serializer = EmployeeSerializer(emp, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


# fetch

def fetch(request):
    emp_fetch = Employee.objects.all()
    return render(request, 'webapp/emp_details.html',{'emp' : emp_fetch})


# to sort records based on the descending order of the score
def sort(request):
    emp_sort = Employee.objects.filter().order_by('-score')
    return render(request, 'webapp/emp_details.html',{'emp' : emp_sort})



# descending order of score in JSON response
def sortJSON(request):
    emp_sort = Employee.objects.filter().order_by('-score')
    serializer = EmployeeSerializer(emp_sort, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


# for every 5th & 6th indices dept should be 'belltech'
from django.shortcuts import render
#from .models import Employee
from .forms import EmpRegister

'''
for displaying form

def showformdata(request):
    fm = EmpRegister()
    return render(request, 'webapp/insert.html',{'form':fm})
'''

# to submit records

def showformdata(request):
    if request.method == 'POST':
        fm = EmpRegister(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['emp_code']
            dept = fm.cleaned_data['department']
            sc = fm.cleaned_data['score']
            dc = fm.cleaned_data['date_created']
            
            reg = Employee(emp_code=nm, department=dept, score=sc, date_created=dc)
            reg.save()

    else:
        fm = EmpRegister()
    
    return render(request, 'webapp/insert.html',{'form':fm})
 

# fetch with chunk parameter size

def fetch_chunk(request,my_id):
    # chunk = len(Employee.emp_code)
    query = request.GET.get('my_id')
    emp_para = Employee.objects.get(pk=my_id)
    return render(request, 'webapp/parameter.html',{'emp': emp_para})
    # return render(request, 'webapp/displayMsg.html')