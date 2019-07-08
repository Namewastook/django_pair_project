from django.db import models

# Create your models here.
class Profile(models.Model):
    first = models.CharField(max_length=50, default="")
    last = models.CharField(max_length=50, default="")
    username = models.CharField(max_length=150, default="")
    aboutyou = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.first