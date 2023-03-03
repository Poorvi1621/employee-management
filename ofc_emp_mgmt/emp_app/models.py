from django.db import models


# Create your models here.

class Department(models.Model):
    Name=models.CharField(max_length=100,null=False)
    location= models.CharField(max_length=100)

    def __str__(self):
         return self.Name

 
class Role(models.Model):
    Name=models.CharField(max_length=100,null=False)

    def __str__(self):
         return self.Name
   
class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    Department=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    Role=models.ForeignKey(Role,on_delete=models.CASCADE)
    hire_date=models.DateField()
    phone=models.IntegerField(default=0)

    def __str__(self):
         return self.first_name