from django.db import models
from django.utils import timezone


class Department(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "department"
        verbose_name_plural = "departments"


class Employee(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=255)
    is_married = models.BooleanField(default=False)
    salary = models.FloatField(default=0.0)
    contract_exp = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.department}"

    class Meta:
        verbose_name = "employee"
        verbose_name_plural = "employees"


class About(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "about"
        verbose_name_plural = "abouts"


class Contact(models.Model):
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.address} | {self.email} | {self.phone}"

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"


class Team(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    position = models.CharField(max_length=55)
    about = models.TextField(max_length=255)
    avatar = models.ImageField(
        upload_to="team")

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.position}"

    class Meta:
        verbose_name = "team"
        verbose_name_plural = "teams"


class Slider(models.Model):
    img = models.ImageField(upload_to="slider")
    title = models.CharField(max_length=255)
    descr = models.TextField(max_length=400)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "slider"
        verbose_name_plural = "sliders"


class SEO(models.Model):
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    keywords = models.CharField(max_length=255)
    robots = models.CharField(max_length=255)
    content_type = models.CharField(max_length=255)
    language = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.tag}"

    class Meta:
        verbose_name = "seo"
        verbose_name_plural = "seo"


class OG(models.Model):
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    type = models.CharField(max_length=255)
    image = models.ImageField(upload_to="og")
    url = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.tag}"

    class Meta:
        verbose_name = "Open Graph"
        verbose_name_plural = "Open Graphs"