# This view can be viewed by every type of users
# Ex:- Homepage, any page that does not want user to login.

from django.shortcuts import render


def index(request):
    return render(request, 'event-management-system/index.html')


def login(request):
    return render(request, 'event-management-system/login.html')

