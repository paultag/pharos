from django.contrib.gis.db import models
from django.db.models import DateTimeField
from django.contrib.auth.models import User


class PharosPoint(models.Model):
    point = models.PointField()
    timestamp = DateTimeField()
    user = models.ForeignKey(User)
    objects = models.GeoManager()
