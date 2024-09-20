from django.contrib import admin
from .models import StudentData
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "state",)

admin.site.register(StudentData,StudentAdmin)

