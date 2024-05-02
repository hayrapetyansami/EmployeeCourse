from django.shortcuts import render
from .models import Department, Employee, About, Contact


def index(request):
    return render(request, "home.html")


def employees(request):
    employees = Employee.objects.all()
    return render(request, "employees.html", {"employees": employees})


def about(request):
    about_text = About.objects.all()
    return render(request, "about.html", {"about_text": about_text})


def contact(request):
    contact_text = Contact.objects.all()
    return render(request, "contact.html", {"contact_text": contact_text})


def single_employee(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    return render(request, "single_employee.html", {"employee": employee})
