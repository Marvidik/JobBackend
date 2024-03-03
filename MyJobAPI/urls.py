from django.contrib import admin
from django.urls import path, re_path
from Authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('login',views.login, name="login"),
    re_path('signup',views.register,name="register"),
    path('password/reset/', views.password_reset, name='password_reset'),
    # re_path("jobs", views.jobs,name="all_jobs")
    
]
