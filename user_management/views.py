from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import *

# Create your views here.
def login_pages(request):
    return render(request,'index.html')

def register_data(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form':form}
        return render(request,'registration.html',context)

def register(request):
    return render(request,'registration.html')
    # if request.method == 'POST':
    #     first_name = request.POST['firstname']
    #     last_name = request.POST['lastname']
    #     username = request.POST['username']
    #     email = request.POST['Email']
    #     password = request.POST['pass']

    #     user = User.objects.create_user(user_name=username, password=password, email=email, first_name=first_name, last_name=last_name)
    #     user.save()
    #     print('user created')
    #     return redirect('')
    # else:
        

def prelogin(request):
    if request.method == 'POST':
        
        username = request.POST['']
        first_name = request.POST['']
        last_name = request.POST['']
        email = request.POST['']
        username.save()
        first_name.save()
        last_name.save()
        email.save()

    return render(request,'sample_loginPage.html')