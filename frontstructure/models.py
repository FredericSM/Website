from django.contrib.auth.models import User
from django.db import models

class MyModel(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    mobile_number = models.IntegerField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)