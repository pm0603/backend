from django.db import models


class Content(models.Model):
    seq = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=100, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    place = models.CharField(max_length=100, null=True)
    realm_name = models.CharField(max_length=10, null=True)
    area = models.CharField(max_length=10, null=True)
    price = models.CharField(max_length=30, null=True)
    content = models.TextField(max_length=5000, null=True)
    ticket_url = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=50, null=True)
    thumbnail = models.CharField(max_length=200, null=True)
    gps_x = models.CharField(max_length=30, null=False)
    gps_y = models.CharField(max_length=30, null=True)
    place_url = models.CharField(max_length=200, null=True)
    place_addr = models.CharField(max_length=100, null=True)
    place_seq = models.CharField(max_length=10, null=True)
