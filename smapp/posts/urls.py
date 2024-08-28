from django.urls import path, include
from .views import new_post

app_name = "mainpage"

urlpatterns = [
    path('new_post', new_post, name="new_post")
]