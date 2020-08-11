from django.db import models

class DateTime(models.Model):
    date_year = models.IntegerField()
    date_month = models.IntegerField()
    date_day = models.IntegerField()
    time_hour = models.IntegerField()
    time_minute = models.IntegerField()
    time_second = models.IntegerField()
