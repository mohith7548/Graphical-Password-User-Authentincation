from django.db import models
from django.contrib.auth.models import User

class LoginInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fails = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username
