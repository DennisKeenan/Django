from django.contrib import admin
from .models import Member

# Register your models here.
class Member_Admin(admin.ModelAdmin):
    list_display=("First_Name","Last_Name","Phone_Number","Join")
admin.site.register(Member,Member_Admin)