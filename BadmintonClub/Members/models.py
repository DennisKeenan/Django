from django.db import models

# Create your models here.
class Member(models.Model):
    First_Name=models.CharField(max_length=15)
    Last_Name=models.CharField(max_length=30)
    Phone_Number=models.IntegerField(null=True)
    Join=models.DateField(null=True)