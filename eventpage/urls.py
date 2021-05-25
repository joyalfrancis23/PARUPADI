from django.urls import path
from . import views
urlpatterns=[
    path('',views.home),
    path('registersuccess/',views.registersuccess),
    path('eventregistration/',views.eventregistration),
]