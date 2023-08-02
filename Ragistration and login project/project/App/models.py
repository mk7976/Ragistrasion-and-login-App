from django.db import models


# Create your models here.
class User(models.Model):
    Username = models.CharField(max_length=10)
    Email = models.EmailField()
    Password = models.CharField(max_length=8)
    Confirm_password = models.CharField(max_length=8)

    def __str__(self):
        return self.Email
