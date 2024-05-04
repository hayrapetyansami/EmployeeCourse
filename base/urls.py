"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.models import DepartmentResource, EmployeeResource
from tastypie.api import Api

api = Api(api_name="v1")
d_resource = DepartmentResource()
e_resource = EmployeeResource()
api.register(d_resource)
api.register(e_resource)

# api/v1/departments
# api/v1/employees

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("employees.urls")),
    path("api/", include(api.urls)),
]
