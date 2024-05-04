from tastypie.resources import ModelResource
from employees.models import Department, Employee
from tastypie.authorization import Authorization
from .auth import CustomAuthentication


class DepartmentResource(ModelResource):
    class Meta:
        queryset = Department.objects.all()
        resource_name = "departments"
        allowed_methods = ["get"]


class EmployeeResource(ModelResource):
    class Meta:
        queryset = Employee.objects.all()
        resource_name = "employees"
        allowed_methods = ["get", "post", "delete"]
        authentication = CustomAuthentication()
        authorization = Authorization()
        excludes = ['contract_exp', 'created_at']

    def hydrate(self, bundle):
        bundle.obj.department_id = bundle.data["department_id"]
        return bundle

    def dehydrate(self, bundle):
        bundle.data["department_id"] = bundle.obj.department
        return bundle

    def dehydrate_email(self, bundle):
        return bundle.data["email"].upper()
