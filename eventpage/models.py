from django.db import models
import datetime

from django.db.models.fields import EmailField
# Create your models here.
class Eventpage(models.Model):
    Event_name=models.CharField(max_length=255)
    Date=models.DateField(blank=True, null=True)
    Time=models.TimeField(blank=True, null=True)
    Event_location=models.CharField(max_length=250)
    Event_Description=models.CharField(max_length=500)
    max_participants=models.IntegerField()
    image=models.CharField(max_length=25000)

class Participants(models.Model):
    Name = models.CharField(max_length=255)
    Branch = models.CharField(max_length=255)
    Semester = models.IntegerField()
    Phone = models.IntegerField()
    Email = models.EmailField()
