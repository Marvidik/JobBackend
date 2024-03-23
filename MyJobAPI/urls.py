from django.contrib import admin
from django.urls import path, re_path
from Authentication import views
from userprofile import views as profileview

urlpatterns = [

    # Urls for all authentications and user profile infos
    path('admin/', admin.site.urls),
    path('login/',views.login, name="login"),
    path('signup/',views.register,name="register"),
    path('password/reset/', views.password_reset, name='password_reset'),
    path('password/reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('create-profile/',profileview.create_profile,name="create-profile"),
    path('profile/<username>/',profileview.view_profile,name="view_profile"),
    # path('profile/<username>/update',profileview.update_profile,name="update-profile"),
    
]
