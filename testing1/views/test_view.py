# This view can be viewed by every type of users
# Ex:- Homepage, any page that does not want user to login.
# from django.contrib import auth, messages
# from django.contrib.auth.decorators import login_required
# # from django.core.urlresolvers import reverse
# # from django.urls import reverse_lazy
# from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
# from django.template.context_processors import csrf
# from django.views.generic import ListView

# from ..models import Event, Association
from django.template.context_processors import csrf
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from EventManagementSystem.decorators import slkf_required, association_required, district_required, province_required
from EventManagementSystem.models import State

associationDecorators = [login_required, association_required]
decorators = [login_required, slkf_required]
districtDecorators = [login_required, district_required]
provinceDecorators = [login_required, province_required]


def index(request):
    return render(request, 'event-management-system/index.html')


@method_decorator(decorators, name='dispatch')
class SlkfPortal(TemplateView):
    template_name = 'event-management-system/slkf/slkfPortal.html'


@method_decorator(associationDecorators, name='dispatch')
class AssociationPortal(ListView):
    template_name = 'event-management-system/association/associationPortal.html'
    model = State
    context_object_name = 'states'

    def get_queryset(self):
        queryset = State.objects.filter(stateID=1)
        return queryset


@method_decorator(districtDecorators, name='dispatch')
class DistrictPortal(TemplateView):
    template_name = 'event-management-system/district/districtPortal.html'


@method_decorator(provinceDecorators, name='dispatch')
class ProvincePortal(TemplateView):
    template_name = 'event-management-system/province/provincePortal.html'


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

        # TODO: following differs from the original code ---> request.user.userType == 'AS'
        if request.POST.user.userType == 'AS':
            return HttpResponseRedirect(reverse_lazy('association-portal'))
        elif request.POST.user.userType == 'DI':
            return HttpResponseRedirect(reverse_lazy('district-portal'))
        elif request.POST.user.userType == 'PR':
            return HttpResponseRedirect(reverse_lazy('province-portal'))
        else:
            return HttpResponseRedirect(reverse_lazy('slkf-portal'))

    else:
        messages.success(request, 'Login failed. Try again.')
        return HttpResponseRedirect(reverse_lazy('login'))


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'Logged out!')
    return HttpResponseRedirect(reverse_lazy('index'))


def tournamentPage(request):
    return render(request, 'event-management-system/tournamentPage.html')

# def tournamentPage(request):
#     return render(request, 'event-management-system/tournamentPage.html')


# class EventsListView(ListView):
#     model = Event
#     context_object_name = 'eventList'
#     template_name = 'event-management-system/generic-user/eventList.html'
#
#     def get_queryset(self):
#         queryset = Event.objects.all()
#         return queryset
#
#
# class AssociationsListView(ListView):
#     model = Association
#     context_object_name = 'associationList'
#     template_name = 'event-management-system/generic-user/associationList.html'
#
#     def get_queryset(self):
#         queryset = Association.objects.all()
#         return queryset
