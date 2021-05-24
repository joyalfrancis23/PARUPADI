from django.shortcuts import render
from .models import Eventpage,Participants
from datetime import datetime

# Create your views here.
def home(request):
    eventpage = Eventpage.objects.all()
    return render(request,'home.html',{'eventpage':eventpage})

def registersuccess(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        branch = request.POST.get('branch')
        sem = request.POST.get('semester')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        obj = Participants()
        obj.Name = name
        obj.Branch = branch
        obj.Semester = sem
        obj.Phone = phone
        obj.Email = email
        obj.save()
        
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