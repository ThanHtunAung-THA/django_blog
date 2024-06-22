from django.db import models
from datetime import datetime

# Create your models here.

class PostModel(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=100)
  body = models.TextField()
  created_at = models.DateTimeField(default=datetime.now)