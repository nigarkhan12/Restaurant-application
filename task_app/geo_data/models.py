from django.db import models

# Create your models here.
class Place(models.Model):
    id=models.IntegerField(primary_key=True)
    location = models.PointField(null=True, blank=True)
    objects = models.GeoManager()