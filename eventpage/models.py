from django.db import models

# Create your models here.
class eventpage(models.Model):
    Event_name=models.CharField(max_length=255)
    Date_Time=models.DateTimeField()
    Event_location=models.CharField(max_length=250)
    Event_Description=models.CharField(max_length=500)
    max_participants=models.IntegerField()
    image=models.CharField(max_length=2500)
