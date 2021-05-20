from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_pages),
    path('register/',views.register),
    path('prelogin/',views.sampleLoginPage),
]
