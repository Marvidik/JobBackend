from django.contrib import admin
from .models import UserProfile,PasswordResetToken

# Register your models here.



admin.site.register(UserProfile)
admin.site.register(PasswordResetToken)