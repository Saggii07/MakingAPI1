from enum import auto
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Advisor(models.Model):
    advisor_name = models.CharField(max_length=50)
    advisor_photo_url = models.URLField(max_length=200)

    def __str__(self):
        return self.advisor_name


class Booking(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    adviser_id = models.ForeignKey(Advisor,on_delete=models.CASCADE)
    booked_call_at = models.DateTimeField()
