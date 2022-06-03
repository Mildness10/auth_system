from statistics import mode
from django.db import models

class Post(models.Model):
    text = models.TextField()
