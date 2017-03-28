from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models



class Performance(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.IntegerField()
    place = models.CharField(max_length=30)
    image_url = models.URLField()
    contact_info = models.CharField(null=True, max_length=30)
    performance_copyright = models.CharField(max_length=30)


class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    performance = models.ForeignKey(Performance)
    created_date = models.DateTimeField(auto_now_add=True)