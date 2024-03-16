from django.contrib import admin
from django.urls import path, re_path
from Authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login, name="login"),
    path('signup/',views.register,name="register"),
    path('password/reset/', views.password_reset, name='password_reset'),
    path('password/reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    

    path('create-profile/',views.profile_add,name="profile"),
    path('get_profile/',views.profile_get,name="get_profile"),

    
]
