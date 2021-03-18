from django.urls import path
from . import views
from django.contrib.auth import login, logout
from apps.login.views import login_form, logout_user


urlpatterns = [
    path('login/', login_form.as_view(), name='login'),
    path('logout/', logout_user.as_view(), name='logout'), # CORREGIR LOGOUT
    # path('logout/', views.logout, name='logout'),
    
]