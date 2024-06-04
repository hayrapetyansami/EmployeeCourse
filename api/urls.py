# api/urls.py

from django.urls import path, include
from tastypie.api import Api
from .models import DepartmentResource, EmployeeResource, TeamResource

api = Api(api_name="v1")
api.register(DepartmentResource())
api.register(EmployeeResource())
api.register(TeamResource())

urlpatterns = [
    path("", include(api.urls), name="index"),
]