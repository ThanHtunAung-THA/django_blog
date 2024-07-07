from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class CategoryModel(models.Model):
  id  = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  created_at = models.DateTimeField(default=datetime.now)

  def __str__(self):
    return self.name

class PostModel(models.Model):
  id = models.AutoField(primary_key=True)
  category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, default=None)
  author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
  image = models.ImageField(default=None, blank=True)
  title = models.CharField(max_length=100)
  body = models.TextField()
  created_at = models.DateTimeField(default=datetime.now)

  def __str__(self):
    return self.title
