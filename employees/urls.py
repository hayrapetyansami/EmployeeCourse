from django.urls import path
from django.contrib.auth import views as auth_views
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
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.signup, name="signup"),
    path("profile/", views.profile, name="profile")
]
