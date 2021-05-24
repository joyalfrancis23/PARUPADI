from django.shortcuts import render
from .models import Eventpage
from datetime import datetime

# Create your views here.
def home(request):
    eventpage = Eventpage.objects.all()
    return render(request,'home.html',{'eventpage':eventpage})

def registersuccess(request):
    return render(request,'registersuccess.html')

def eventregistration(request):
    if request.method == 'POST':
        title = request.POST.get('eventname')
        date = request.POST.get('eventdate')
        time = request.POST.get('eventtime')
        location = request.POST.get('eventlocation')
        description = request.POST.get('eventdescription')
        max_participants = request.POST.get('maxparticipants')
        image_url = request.POST.get('imageurl')
        print(title,date,time,location,description,max_participants,image_url)
        obj = Eventpage()
        obj.Event_name = title
        obj.Date = date
        obj.Time = time
        obj.Event_location = location
        obj.Event_Description = description
        obj.max_participants = max_participants
        obj.image = image_url
        obj.save()

    return render(request,'eventregistration.html')