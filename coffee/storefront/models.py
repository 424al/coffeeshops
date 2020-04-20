from django.db import models

# Create your models here.

class StoreFronts(models.Model):
    name = models.CharField(max_length=250, blank=False)