from django.shortcuts import render
from .models import (
    Department,
    Employee,
    About,
    Contact,
    Team,
    Slider,
    SEO,
    OG
)


def index(request):
    slides = Slider.objects.all()
    seo = SEO.objects.filter(tag="home")
    og = OG.objects.filter(tag="home")
    return render(request, "home.html", {
        "slides": slides,
        "seo": seo,
        "og": og
    })


def employees(request):
    employees = Employee.objects.all()
    seo = SEO.objects.filter(tag="employees")
    og = OG.objects.filter(tag="employees")
    return render(request, "employees.html", {
        "employees": employees,
        "seo": seo,
        "og": og
    })


def about(request):
    about_text = About.objects.all()
    team = Team.objects.all()
    seo = SEO.objects.filter(tag="about")
    og = OG.objects.filter(tag="about")
    return render(request, "about.html", {
        "about_text": about_text,
        "team": team,
        "seo": seo,
        "og": og
    })


def contact(request):
    contact_text = Contact.objects.all()
    seo = SEO.objects.filter(tag="contact")
    og = OG.objects.filter(tag="contact")

    return render(request, "contact.html", {
        "contact_text": contact_text,
        "seo": seo,
        "og": og
    })


def single_employee(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    seo = SEO.objects.filter(tag="single_employee")
    og = OG.objects.filter(tag="single_employee")
    return render(request, "single_employee.html", {
        "employee": employee,
        "seo": seo,
        "og": og
    })


def single_member(request, member_id):
    member = Team.objects.get(pk=member_id)
    seo = SEO.objects.filter(tag="single_member")
    og = OG.objects.filter(tag="single_member")
    return render(request, "single_member.html", {
        "member": member,
        "seo": seo,
        "og": og
    })
