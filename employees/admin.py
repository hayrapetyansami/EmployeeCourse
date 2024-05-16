from django.contrib import admin
from .models import (Department, Employee, About, Contact, Team)

admin.site.site_header = "Employees Admin"
admin.site.site_title = "Employees Admin Panel"
admin.site.index_title = "Welcome dear Employees Admin"


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",
                    "email", "salary", "is_married", "id")


class EmployeeInline(admin.TabularInline):
    model = Employee
    exclude = ["contract_exp", "created_at"]
    extra = 1


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("title", "id")
    fieldsets = [
        (None, {"fields": ["title"]}),
        ("Dates", {
            "fields": ["created_at"],
            "classes": ["collapse"]
        })
    ]
    inlines = [EmployeeInline]


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Team)
