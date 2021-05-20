from django.shortcuts import render
from django.http import HttpResponse
from .models import eventpage
# Create your views here.
def home(request):
    eventpage = eventpage.objects.all()
    return render(request,'home.html',{'eventpage':eventpage})
   #return HttpResponse("<h1>Event Page</h1>")
