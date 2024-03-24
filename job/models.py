from django.db import models

# Create your models here.

class Jobs(models.Model):
    job_title=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    company_logo=models.ImageField(upload_to="company-logos")
    salary_range=models.CharField(max_length=100, blank=True)
    job_description=models.TextField()
    job_requirements=models.CharField(max_length=300)
