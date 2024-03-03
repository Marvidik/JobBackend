from django.db import models

# Create your models here.


class Jobs(models.Model):
    jobtitle=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    companylogo=models.URLField()
    date=models.CharField(max_length=100)



class Profile(models.Model):
    pass