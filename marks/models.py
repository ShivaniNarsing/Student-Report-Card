from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='images')
    roll_number=models.CharField(max_length=10,blank=True)
    marks=models.CharField(max_length=100)
    grade=models.CharField(max_length=1)
    result=models.CharField(max_length=100)

    def __str__(self):
            return self.first_name