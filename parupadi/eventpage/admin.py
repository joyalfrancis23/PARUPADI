from django.contrib import admin
from .models import Eventpage
class EventpageAdmin(admin.ModelAdmin):
    list_display = ('Event_name','Date','Time','Event_location','max_participants')
# Register your models here.
admin.site.register(Eventpage,EventpageAdmin)
