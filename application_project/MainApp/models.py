from django.db import models
from django.contrib.auth.models import User
import geocoder

# Create your models here.


class Places(models.Model):
    author = models.ForeignKey(User, on_delete= models.DO_NOTHING)
    place_name = models.CharField(blank=True, null=True, max_length=255, verbose_name='Название места')
    comment = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)




