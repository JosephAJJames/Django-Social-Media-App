from django.urls import path, include
from . import views

app_name = "comments"

urlpatterns = [
    path('new_comment', views.new_comment, name="new_comment")
]