    # Python-basic
    # Run server by using python manage.py runserver

    # Admin user name : try3
    # Password : try3

    # 1
    # use URL http://127.0.0.1:8000/EmpInfo_JSON/
    # the above URL will retrieve the JSON data

    # 2
    # use URL http://127.0.0.1:8000/sort/emp_sorted/
    # the above URL will fetch the employee records

    # 3
    # use URL http://127.0.0.1:8000/EmpSort_JSON/
    # the above URL will fetch the employee records

    # 4
    # use URL http://127.0.0.1:8000/reg/registration/
    # the above URL will to insert records using form
    path('reg/', include('webapp.urls')),

    # 5
    # use URL http://127.0.0.1:8000/insert/registration/
    # the above URL will to insert records using form

    # 6
    # use URL http://127.0.0.1:8000/chunk/para/
    # after http://127.0.0.1:8000/chunk/para/  type integer in URL
    # the above URL is having query parameter
