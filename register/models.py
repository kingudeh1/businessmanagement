from django.db import models

class Person(models.Model):
    surname = models.CharField(max_length=100,null=True,blank=True)
    middlename = models.CharField(max_length=100,null=True,blank=True)
    lastname = models.CharField(max_length=100,null=True,blank=True)
    faculty = models.CharField(max_length=100,null=True,blank=True)
    department = models.CharField(max_length=100,null=True,blank=True)
    sex = models.CharField(max_length=6,null=True,blank=True)  # Male/Female
    matric_number = models.CharField(max_length=20,null=True,blank=True)
    level = models.CharField(max_length=10,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=15,null=True,blank=True)


    def __str__(self):
        return self.surname
