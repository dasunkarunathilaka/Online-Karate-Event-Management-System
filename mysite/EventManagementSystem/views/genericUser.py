# This view can be viewed by every type of users
# Ex:- Homepage, any page that does not want user to login.
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views.generic import ListView

from ..models import Event, Association


def index(request):
    return render(request, 'event-management-system/index.html')


@login_required
def signupSuccess(request):
    return render(request, 'event-management-system/registration/signupSuccess.html')


def customLogin(request):
    # To identify whether a user has already logged in or not.
    if request.user.is_authenticated():
        return HttpResponseRedirect('/event-management-system/')
    else:
        return userLogin(request)


def userLogin(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'event-management-system/user-login/login.html', c)


def userAuth(request):
    # When user submits the login form, it comes here.
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    # If there is no value returned, empty string is returned by the second parameter.

    user = auth.authenticate(username=username, password=password)
    # If there is no user matching username and password, return None object. None = Null

    if user is not None:
        auth.login(request, user)
        # Set the current user's status to logged in.

        # Following returns a url... it will be checked in the urls.py to decide what to do.
        # render returns a html page. So the correct path should be given to that file.
        return HttpResponseRedirect('loggedin')
    # user is already in the 'movieratingapp/accounts/' url. we need to give the next location only.

    else:
        return HttpResponseRedirect('invalid')


@login_required
def loggedin(request):
    return render(request, 'event-management-system/user-login/loggedin.html', {'user_name': request.user.first_name})


def invalidLogin(request):
    return render(request, 'event-management-system/user-login/invalid.html')


@login_required
def logout(request):
    auth.logout(request)
    return render(request, 'event-management-system/user-login/logout.html')


def tournamentPage(request):
    return render(request, 'event-management-system/tournamentPage.html')


class EventsListView(ListView):
    model = Event
    context_object_name = 'eventList'
    template_name = 'event-management-system/generic-user/eventList.html'

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset


class AssociationsListView(ListView):
    model = Association
    context_object_name = 'associationList'
    template_name = 'event-management-system/generic-user/associationList.html'

    def get_queryset(self):
        queryset = Association.objects.all()
        return queryset
