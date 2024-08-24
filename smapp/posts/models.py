from django.db import models
from users.models import User


# Create your models here.
class Post(models.Model):
    text: str = models.TextField()
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)