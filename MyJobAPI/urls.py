from django.contrib import admin
from django.urls import path, re_path

from Authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('login',views.login),
    re_path('signup',views.register),
    re_path("jobs", views.jobs,name="all_jobs")
    
]
