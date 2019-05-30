from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, ListView, View

# This is a class based view. Instead of using a method as a view, this whole class can be used.
# as_view() method needs to be called (inherited from CreateView) in the urls.py

# TODO: forms have the error
# from .. import slkfSignupForm
from EventManagementSystem.forms.eventCreationForm import EventCreationForm
from EventManagementSystem.decorators import slkf_required
from EventManagementSystem.forms.slkfSignupForm import SlkfSignupForm
from EventManagementSystem.models import User, Event, Association, Slkf, District, Province, Player, Coach, State

decorators = [login_required, slkf_required]


# Decorators are added to prevent unauthorized users getting these views via typing url in the browser.
@method_decorator(decorators, name='dispatch')
class SignUpDirectingView(TemplateView):
    template_name = 'event-management-system/signupDirect.html'


@method_decorator(decorators, name='dispatch')
class SlkfSignUpView(CreateView):
    model = User
    form_class = SlkfSignupForm
    template_name = 'event-management-system/registration/userCreationForm.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'SLKF User'
        return super(SlkfSignUpView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'New SLKF user created successfully!')
        return HttpResponseRedirect(reverse_lazy('slkf-users'))


@method_decorator(decorators, name='dispatch')
class SlkfPortal(TemplateView):
    template_name = 'event-management-system/slkf/slkfPortal.html'


@method_decorator(decorators, name='dispatch')
class EventCreationView(CreateView):
    model = Event
    form_class = EventCreationForm
    template_name = 'event-management-system/slkf/eventCreation.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'New Event created successfully!')
        return HttpResponseRedirect(reverse_lazy('all-events-players'))


# @method_decorator(decorators, name='dispatch')
class AssociationsListView(ListView):
    model = Association
    context_object_name = 'associationList'
    template_name = 'event-management-system/slkf/associationList.html'

    def get_queryset(self):
        queryset = Association.objects.all()
        return queryset


@method_decorator(decorators, name='dispatch')
class SlkfUsersListView(ListView):
    model = Slkf
    context_object_name = 'slkfUserList'
    template_name = 'event-management-system/slkf/slkfUserList.html'

    def get_queryset(self):
        queryset = Slkf.objects.all()
        return queryset


@method_decorator(decorators, name='dispatch')
class DistrictUsersListView(ListView):
    model = District
    context_object_name = 'districtUserList'
    template_name = 'event-management-system/slkf/districtUserList.html'

    def get_queryset(self):
        queryset = District.objects.all()
        return queryset


@method_decorator(decorators, name='dispatch')
class ProvinceUsersListView(ListView):
    model = Province
    context_object_name = 'provinceUserList'
    template_name = 'event-management-system/slkf/provinceUserList.html'

    def get_queryset(self):
        queryset = Province.objects.all()
        return queryset


# List players for each association for the SLKF user view.
# @method_decorator(decorators, name='dispatch')
class PlayersListByAssociationView(ListView):
    model = Player
    context_object_name = 'playerList'
    template_name = 'event-management-system/association/playerList.html'

    # request.session['my_thing'] = my_thing

    def get_queryset(self):
        queryset = Player.objects.filter(association__user__username=self.request.GET.get('association', ""))
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['association'] = self.request.GET.get('association', "")
        # self.request.session['association'] = "d"
        return super(PlayersListByAssociationView, self).get_context_data(**kwargs)


# List coaches for each association for the SLKF user view.
# @method_decorator(decorators, name='dispatch')
class RegisteredCoachSlkfListView(ListView):
    model = Coach
    context_object_name = 'coachList'
    template_name = 'event-management-system/association/coachList.html'

    def get_queryset(self):
        queryset = Coach.objects.filter(association__user__username=self.request.GET.get('association', ""))
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['association'] = self.request.GET.get('association', "")
        return super(RegisteredCoachSlkfListView, self).get_context_data(**kwargs)


# List all the players
@method_decorator(decorators, name='dispatch')
class AllPlayersListView(ListView):
    model = Player
    context_object_name = 'playerList'
    template_name = 'event-management-system/slkf/playerList.html'

    def get_queryset(self):
        queryset = Player.objects.all()
        return queryset


# List players on events.
# @method_decorator(decorators, name='dispatch')
class PlayersListByEventView(ListView):
    model = Player
    context_object_name = 'playerList'
    template_name = 'event-management-system/slkf/playersByEvent.html'

    def get_queryset(self):
        queryset = Player.objects.filter(event__eventID=self.request.GET.get('event', ""))
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['event'] = self.request.GET.get('event', "")
        return super(PlayersListByEventView, self).get_context_data(**kwargs)


# List players on districts.
@method_decorator(decorators, name='dispatch')
class PlayersListByDistrictView(ListView):
    model = Player
    context_object_name = 'playerList'
    template_name = 'event-management-system/slkf/playersByDistrict.html'

    def get_queryset(self):
        queryset = Player.objects.filter(district__user__username=self.request.GET.get('district', ""))
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['district'] = self.request.GET.get('district', "")
        return super(PlayersListByDistrictView, self).get_context_data(**kwargs)


# List players on provinces.
@method_decorator(decorators, name='dispatch')
class PlayersListByProvinceView(ListView):
    model = Player
    context_object_name = 'playerList'
    template_name = 'event-management-system/slkf/playersByProvince.html'

    def get_queryset(self):
        queryset = Player.objects.filter(district__province__user__username=self.request.GET.get('province', ""))
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['province'] = self.request.GET.get('province', "")
        return super(PlayersListByProvinceView, self).get_context_data(**kwargs)


@method_decorator(decorators, name='dispatch')
class OpenTournament(View):
    model = State

    def get(self, request, *args, **kwargs):
        queryset = State.objects.all()

        if queryset.count() != 1:
            State(stateID=1, isOpen=True).save()

        else:
            obj = State.objects.get(stateID=1)
            obj.isOpen = True
            obj.save()

        messages.success(request, 'Tournament registration opened!')
        return HttpResponseRedirect(reverse_lazy('slkf-portal'))


@method_decorator(decorators, name='dispatch')
class CloseTournament(View):
    model = State

    def get(self, request, *args, **kwargs):
        queryset = State.objects.all()

        if queryset.count() != 1:
            messages.success(request, 'Tournament not opened yet!')

        else:
            obj = State.objects.get(stateID=1)
            obj.isOpen = False
            obj.save()
            messages.success(request, 'Tournament registration closed!')

        return HttpResponseRedirect(reverse_lazy('slkf-portal'))


# ------------------------------------------------------------------------------

@method_decorator(decorators, name='dispatch')
class EventsListViewForEvents(ListView):
    model = Event
    context_object_name = 'eventList'
    template_name = 'event-management-system/slkf/eventListWithPlayersbtn.html'

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset


@method_decorator(decorators, name='dispatch')
class EventsListViewForDraws(ListView):
    model = Event
    context_object_name = 'eventList'
    template_name = 'event-management-system/slkf/eventListWithDrawsbtn.html'

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset


# List players on events as A list before shuffling.
@method_decorator(decorators, name='dispatch')
class PlayersListByEventViewBeforeShuffle(ListView):
    model = Player
    context_object_name = 'playerList'
    template_name = 'draw/index-draw.html'

    def get_queryset(self):
        queryset = Player.objects.filter(event__eventID=self.request.GET.get('event', ""))
        beforeList = []
        for i in queryset:
            a = [str(i.id), str(i.association.user.username), str(i.playerName)]
            beforeList.append(a)

        # code for shuffling on association
        d = dict()
        for player in beforeList:
            if player[1] in d:
                d[player[1]].append([player[0], player[2]])
            else:
                d.setdefault(player[1], [])
                d[player[1]].append([player[0], player[2]])

        afterList = []
        while d != {}:
            for asso in list(d.keys()):
                afterList.append(d[asso][0])
                d[asso].remove(d[asso][0])
                if not d[asso]:
                    del d[asso]
                if d == {}:
                    break
        if len(afterList) == 0:
            return queryset
        return afterList

    def get_context_data(self, **kwargs):
        kwargs['event'] = self.request.GET.get('event', "")
        return super(PlayersListByEventViewBeforeShuffle, self).get_context_data(**kwargs)
