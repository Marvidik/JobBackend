from django.db import models

# Create your models here.


class Jobs(models.Model):
    jobtitle=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    salary=models.IntegerField()
    companylogo=models.ImageField()
    level=models.IntegerField()
    duration=models.CharField(max_length=100)
