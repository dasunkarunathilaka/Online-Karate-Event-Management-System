from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, ListView

from ..decorators import slkf_required, district_required
from ..models import User, Player, Coach, Event
from ..forms.districtSignupForm import DistrictSignupForm

slkfDecorators = [login_required, slkf_required]
districtDecorators = [login_required, district_required]


@method_decorator(slkfDecorators, name='dispatch')
class DistrictSignUpView(CreateView):
    model = User
    form_class = DistrictSignupForm
    template_name = 'event-management-system/registration/districtSignupForm.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'District'
        return super(DistrictSignUpView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return HttpResponseRedirect('signup-success')


@method_decorator(districtDecorators, name='dispatch')
class DistrictPortal(TemplateView):
    template_name = 'event-management-system/district/districtPortal.html'


@method_decorator(districtDecorators, name='dispatch')
class DistrictPlayersListView(ListView):
    model = Player
    context_object_name = 'playerList'
    template_name = 'event-management-system/slkf/playersByDistrict.html'

    def get_queryset(self):
        queryset = Player.objects.filter(district__user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['district'] = self.request.user.username
        return super(DistrictPlayersListView, self).get_context_data(**kwargs)


@method_decorator(districtDecorators, name='dispatch')
class DistrictCoachesListView(ListView):
    model = Coach
    context_object_name = 'coachList'
    template_name = 'event-management-system/district/coachList.html'

    def get_queryset(self):
        queryset = Coach.objects.all()
        return queryset


@method_decorator(districtDecorators, name='dispatch')
class DistrictEventsListView(ListView):
    model = Event
    context_object_name = 'eventList'
    template_name = 'event-management-system/district/districtEventList.html'

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset


@method_decorator(districtDecorators, name='dispatch')
class DistrictPlayersByEventListView(ListView):
    model = Player
    context_object_name = 'playerList'
    template_name = 'event-management-system/slkf/playersByEvent.html'

    def get_queryset(self):
        queryset = Player.objects.filter(event__eventID=self.request.GET.get('event', ""),
                                         district__user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['event'] = self.request.GET.get('event', "")
        return super(DistrictPlayersByEventListView, self).get_context_data(**kwargs)
