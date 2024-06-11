from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.translation import activate, get_language
from django.utils import translation
from django.views.decorators.http import require_POST
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import SignUpForm

from .models import (
    Employee,
    About,
    Contact,
    Team,
    Slider,
    SEO,
    OG,
)


def index(request):
    slides = Slider.objects.all()
    seo = SEO.objects.filter(tag="home")
    og = OG.objects.filter(tag="home")
    return render(request, "home.html", {
        "slides": slides,
        "seo": seo,
        "og": og,
        "request": request
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


@require_POST
def change_lang(request):
    language = request.POST.get("language")
    if language:
        activate(language)
        request.session[translation.LANGUAGE_SESSION_KEY] = language
        return JsonResponse({"success": True, "language": get_language()})
    return JsonResponse({"success": False})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect("app:profile")
            else:
                messages.error(request, "Auth Error")
        else:
            messages.error(request, "Form is not valid")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


@login_required
def profile(request):
    return render(request, "profile.html")
