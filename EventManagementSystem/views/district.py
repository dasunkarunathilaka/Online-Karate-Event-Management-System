from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, ListView

from EventManagementSystem.decorators import slkf_required, district_required
from EventManagementSystem.models import User, Player, Coach, Event
from EventManagementSystem.forms.districtSignupForm import DistrictSignupForm

slkfDecorators = [login_required, slkf_required]
districtDecorators = [login_required, district_required]


@method_decorator(slkfDecorators, name='dispatch')
class DistrictSignUpView(CreateView):
    model = User
    form_class = DistrictSignupForm
    template_name = 'event-management-system/registration/userCreationForm.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'District'
        return super(DistrictSignUpView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'New District user created successfully!')
        return HttpResponseRedirect(reverse_lazy('district-users'))


@method_decorator(districtDecorators, name='dispatch')
class DistrictPortal(TemplateView):
    template_name = 'event-management-system/district/districtPortal.html'


@method_decorator(districtDecorators, name='dispatch')
class DistrictPlayersListView(ListView):
    model = Player
    context_object_name = 'playerList'
    template_name = 'event-management-system/object-lists/playerList.html'

    def get_queryset(self):
        queryset = Player.objects.filter(district__user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['institute'] = self.request.user.username
        return super(DistrictPlayersListView, self).get_context_data(**kwargs)


@method_decorator(districtDecorators, name='dispatch')
class DistrictCoachesListView(ListView):
    model = Coach
    context_object_name = 'coachList'
    template_name = 'event-management-system/object-lists/coachList.html'

    def get_queryset(self):
        queryset = Coach.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['institute'] = self.request.user.username
        return super(DistrictCoachesListView, self).get_context_data(**kwargs)


@method_decorator(districtDecorators, name='dispatch')
class DistrictEventsListView(ListView):
    model = Event
    context_object_name = 'eventList'
    template_name = 'event-management-system/object-lists/eventListWithPlayersbtn.html'

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset


@method_decorator(districtDecorators, name='dispatch')
class DistrictPlayersByEventListView(ListView):
    model = Player
    context_object_name = 'playerList'
    template_name = 'event-management-system/object-lists/playerList.html'

    def get_queryset(self):
        queryset = Player.objects.filter(event__eventID=self.request.GET.get('event', ""),
                                         district__user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['institute'] = self.request.GET.get('event', "")
        return super(DistrictPlayersByEventListView, self).get_context_data(**kwargs)
