from django.urls import path, include
from .models import DepartmentResource, EmployeeResource
from tastypie.api import Api

api = Api(api_name="v1")
d_resource = DepartmentResource()
e_resource = EmployeeResource()
api.register(d_resource)
api.register(e_resource)


urlpatterns = [
    path("", include(api.urls), name="index")
]
