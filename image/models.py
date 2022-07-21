from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Img(models.Model):
    url = models.CharField(max_length=350)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='imgs')

