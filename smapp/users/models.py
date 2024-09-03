from django.db import models
from django.db.models import Model, ForeignKey, CASCADE
from django.contrib.auth.models import AbstractUser
from profilepics.models import ProfilePic
# Create your models here.

class User(AbstractUser):
    profilepic = ForeignKey(ProfilePic, on_delete=models.SET_NULL, related_name="pfp", null=True)

class Followers(models.Model):
    follower = ForeignKey(User, blank=False, null=False, on_delete=CASCADE, related_name="following")
    followed = ForeignKey(User, blank=False, null=False, on_delete=CASCADE, related_name="followers")