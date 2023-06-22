from django.db import models

# Create your models here.
class Restaurants(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    items  = models.JSONField(default=dict)