from django.shortcuts import render
from django.http import HttpResponse
from .models import Eventpage

# Create your views here.
def home(request):
    eventpage = Eventpage.objects.all()
    return render(request,'home.html',{'eventpage':eventpage})
  # return HttpResponse("<h1>event page</h1>")
