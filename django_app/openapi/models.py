from django.db import models


class ContentList(models.Model):
    seq = models.CharField(max_length=2, unique=True)
    title = models.CharField(max_length=100, null=True)
    startDate = models.CharField(max_length=10, null=True)
    endDate = models.CharField(max_length=10, null=True)
    place = models.CharField(max_length=100, null=True)
    realmName = models.CharField(max_length=10, null=True)
    area = models.CharField(max_length=10, null=True)
    price = models.CharField(max_length=30, null=True)
    content = models.CharField(max_length=5000, null=True)
    ticket_url = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=50, null=True)
    thumbnail = models.CharField(max_length=200, null=True)
    gpsX = models.CharField(max_length=30, null=True)
    gpsY = models.CharField(max_length=30, null=True)
    placeUrl = models.CharField(max_length=200, null=True)
    placeAddr = models.CharField(max_length=100, null=True)
    placeSeq = models.CharField(max_length=10, null=True)
