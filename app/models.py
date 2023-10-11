from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    Sname=models.CharField(max_length=100)
    Sprincipal=models.CharField(max_length=100)
    Slocation=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Sname

class Student(models.Model):
    Stuname=models.CharField(max_length=100)
    Stuage=models.IntegerField()
    Sname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='schools')

    def __str__(self) -> str:
        return self.Stuname
    
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
