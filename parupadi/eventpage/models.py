from django.db import models
import datetime
# Create your models here.
class Eventpage(models.Model):
    Event_name=models.CharField(max_length=255)
    Date=models.DateField(blank=True, null=True)
    Time=models.TimeField(blank=True, null=True)
    Event_location=models.CharField(max_length=250)
    Event_Description=models.CharField(max_length=500)
    max_participants=models.IntegerField()
    image=models.CharField(max_length=25000)
