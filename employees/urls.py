from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('employees/', views.employees, name="employees"),
    path('employees/<int:employee_id>',
         views.single_employee, name="single_employee")
]
