from django.contrib import admin
from .models import Student

@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display=['name','email','age','enrollment_date']