from django.shortcuts import render
from .models import Eventpage

# Create your views here.
def home(request):
    eventpage = Eventpage.objects.all()
    return render(request,'home.html',{'eventpage':eventpage})

def registersuccess(request):
    return render(request,'registersuccess.html')

def eventregistration(request):
    return render(request,'eventregistration.html');