from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Restaurant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)