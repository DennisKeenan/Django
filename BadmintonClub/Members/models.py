from django.db import models

# Create your models here.
class Member(models.Model):
    First_Name=models.CharField(max_length=15)
    Last_Name=models.CharField(max_length=30)
    Phone_Number=models.CharField(null=True,max_length=20)
    Join=models.DateField(null=True)
    
    def __str__(self) -> str:
        return f"{self.First_Name} {self.Last_Name}" 