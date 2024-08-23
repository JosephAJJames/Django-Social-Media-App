from django.contrib import admin
from django.urls import path
from .views import login_user, register_user

app_name = "users"

urlpatterns = [
    path('login/', login_user, name="login"),
    path('signup/', register_user, name="signup")
]