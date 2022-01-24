from statistics import mode
from django.db import models

class blogConfig(models.Model):
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=200)
