from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'event-management-system/index.html')


def login(request):
    return render(request, 'event-management-system/login.html')
