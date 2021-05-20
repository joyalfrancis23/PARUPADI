from django.contrib import admin
from .models import eventpage
class eventpageAdmin(admin.ModelAdmin):
    list_display = ('Event_name','Date_Time','Event_location','Event_Description','max_participants')
# Register your models here.
admin.site.register(eventpage,eventpageAdmin)
