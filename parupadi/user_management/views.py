from django.shortcuts import render


# Create your views here.
def login_pages(request):
    return render(request,'index.html')

def register(request):
    return render(request,'registration.html')

