from django.db import models


# Create your models here.
class MyForm(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.BooleanField()
    phoneno = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    district = models.CharField(max_length=250)
    branch = models.CharField(max_length=250)

    def __str__(self):
        return self.name
