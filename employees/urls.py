from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('employees/', views.employees, name="employees"),
    path('employees/<int:employee_id>/',
         views.single_employee, name="single_employee"),
    path('about/<int:member_id>/', views.single_member, name="single_member"),
    path('change_lang/', views.change_lang, name='change_lang'),
]
