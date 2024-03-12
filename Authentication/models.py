from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Basic Information
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)  # Consider using User.email for consistency
    phone_number = models.CharField(max_length=15, blank=True)  # Optional phone number

    # Location (optional)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True) 

    # Job-Specific Information
    resume = models.FileField(upload_to='resumes/', blank=True)  
    cover_letter = models.TextField(blank=True)  
    skills = models.CharField(max_length=255, blank=True)  
    work_experience = models.TextField(blank=True) 
    # Additional Information (optional)
    linkedin_url = models.URLField(blank=True) 
    X_url = models.URLField(blank=True)  
    portfolio_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"