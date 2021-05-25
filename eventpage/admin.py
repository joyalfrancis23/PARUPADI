from django.contrib import admin
from .models import Eventpage,Participants
class EventpageAdmin(admin.ModelAdmin):
    list_display = ('Event_name','Date','Time','Event_location','max_participants')
  
class ParticipantsAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Title','Branch', 'Semester', 'Phone', 'Email')


# Register your models here.
admin.site.register(Eventpage,EventpageAdmin)
admin.site.register(Participants,ParticipantsAdmin)
