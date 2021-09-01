from django.contrib import admin
from django.urls import path, include

from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),


    # 1
    # use URL http://127.0.0.1:8000/EmpInfo_JSON/
    # the above URL will retrieve the JSON data
    path('EmpInfo_JSON/', views.EmployeeDetail),


    # 2
    # use URL http://127.0.0.1:8000/sort/emp_sorted/
    # the above URL will fetch the employee records
    path('sort/', include('webapp.urls')),

    
    
    # 3
    # use URL http://127.0.0.1:8000/EmpSort_JSON/
    # the above URL will fetch the employee records
    path('EmpSort_JSON/', views.sortJSON),


    # 4
    # use URL http://127.0.0.1:8000/reg/registration/
    # the above URL will to insert records using form
    path('reg/', include('webapp.urls')),


    # 5
    # use URL http://127.0.0.1:8000/insert/registration/
    # the above URL will to insert records using form
    path('insert/', include('webapp.urls')),

    
    # 6
    # use URL http://127.0.0.1:8000/chunk/para/
    # after http://127.0.0.1:8000/chunk/para/  type integer in URL
    # the above URL is having query parameter
    path('chunk/', include('webapp.urls')),

]
