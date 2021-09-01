from django.db.models import query
from django.urls import path
from . import views

urlpatterns = [
    path('emp/', views.fetch),



    path('emp_sorted/', views.sort),


    path('registration/', views.showformdata),

    

    path('para/<my_id>', views.fetch_chunk),


]