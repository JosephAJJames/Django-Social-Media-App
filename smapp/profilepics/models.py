from django.db import models
from django.db.models import Model, ImageField


# Create your models here.
class ProfilePic(models.Model):
    image = models.ImageField(upload_to = 'profilepics/images', blank=False, null=False)
    is_default = models.BooleanField(default=False ,null=False, blank=False)