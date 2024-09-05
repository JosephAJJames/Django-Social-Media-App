from django.contrib import admin
from django.urls import path
from .views import login_user, register_user, edit_profile, search_profile, add_follower

app_name = "users"

urlpatterns = [
    path('login/', login_user, name="login"),
    path('signup/', register_user, name="signup"),
    path('edit_profile/', edit_profile, name="edit_profile"),
    path('search_profile/', search_profile, name="search_profile"),
    path('add_follower/', add_follower, name="add_follower")
]