# This view can be viewed by every type of users
# Ex:- Homepage, any page that does not want user to login.
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views.generic import ListView

from ..models import Event, Association


def index(request):
    return render(request, 'event-management-system/index.html')


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

        messages.success(request, 'Logged in successfully.')
        if request.user.userType == 'AS':
            return HttpResponseRedirect(reverse('association-portal'))
        elif request.user.userType == 'DI':
            return HttpResponseRedirect(reverse('district-portal'))
        elif request.user.userType == 'PR':
            return HttpResponseRedirect(reverse('province-portal'))
        else:
            return HttpResponseRedirect(reverse('slkf-portal'))

    else:
        messages.success(request, 'Login failed. Try again.')
        return HttpResponseRedirect(reverse('login'))


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'Logged out!')
    return HttpResponseRedirect(reverse('index'))


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
