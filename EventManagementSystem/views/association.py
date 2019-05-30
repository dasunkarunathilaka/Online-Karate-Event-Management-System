from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, ListView

from EventManagementSystem.forms.coachRegistrationForm import CoachRegistrationForm
from EventManagementSystem.forms.playerRegistrationForm import PlayerRegistrationForm
from EventManagementSystem.decorators import slkf_required, association_required, association_or_slkf_required
from EventManagementSystem.models import User, Event, Player, Coach, State, Association
from EventManagementSystem.forms.associationSignupForm import AssociationSignupForm

slkfDecorators = [login_required, slkf_required]
associationDecorators = [login_required, association_required]
associationOrSlkfDecorators = [login_required, association_or_slkf_required]


@method_decorator(slkfDecorators, name='dispatch')
class AssociationSignUpView(CreateView):
    model = User
    form_class = AssociationSignupForm
    template_name = 'event-management-system/registration/userCreationForm.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Association'
        return super(AssociationSignUpView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'New Association user created successfully!')
        return HttpResponseRedirect(reverse_lazy('association-list'))


@method_decorator(associationDecorators, name='dispatch')
class AssociationPortal(ListView):
    template_name = 'event-management-system/association/associationPortal.html'
    model = State
    context_object_name = 'states'

    def get_queryset(self):
        queryset = State.objects.filter(stateID=1)
        return queryset


@method_decorator(associationOrSlkfDecorators, name='dispatch')
class PlayerRegistrationView(CreateView):
    model = Player
    form_class = PlayerRegistrationForm
    template_name = 'event-management-system/association/playerRegistrationForm.html'

    # Need to pass the currently logged in user to player registration form.
    # Player registration form have the Association column filled automatically.
    def get_form_kwargs(self):
        kwargs = super(PlayerRegistrationView, self).get_form_kwargs()
        if self.request.user.userType == 'AS':
            kwargs.update({'user': self.request.user})
        else:
            associationID = self.request.GET.get('association', "")
            association = User.objects.filter(username=associationID)
            associationList = list(association).pop(0)
            kwargs.update({'user': associationList})
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'New player added successfully!')
        if self.request.user.userType == 'AS':
            return HttpResponseRedirect(reverse_lazy('view-players'))
        else:
            return HttpResponseRedirect(reverse_lazy('slkf-portal'))


@method_decorator(associationDecorators, name='dispatch')
class RegisteredPlayerListView(ListView):
    model = Player
    context_object_name = 'playerList'
    template_name = 'event-management-system/object-lists/playerList.html'

    def get_queryset(self):
        queryset = Player.objects.filter(association=self.request.user.association)
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['institute'] = self.request.user.username
        kwargs['states'] = State.objects.filter(stateID=1)
        return super(RegisteredPlayerListView, self).get_context_data(**kwargs)


@method_decorator(associationDecorators, name='dispatch')
class CoachRegistrationView(CreateView):
    model = Coach
    form_class = CoachRegistrationForm
    template_name = 'event-management-system/association/coachRegistrationForm.html'

    def get_form_kwargs(self):
        kwargs = super(CoachRegistrationView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'New coach added successfully!')
        if self.request.user.userType == 'AS':
            return HttpResponseRedirect(reverse_lazy('view-coaches'))
        else:
            return HttpResponseRedirect(reverse_lazy('slkf-portal'))


@method_decorator(associationDecorators, name='dispatch')
class RegisteredCoachListView(ListView):
    model = Coach
    context_object_name = 'coachList'
    template_name = 'event-management-system/object-lists/coachList.html'

    def get_queryset(self):
        queryset = Coach.objects.filter(association=self.request.user.association)
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['institute'] = self.request.user.username
        return super(RegisteredCoachListView, self).get_context_data(**kwargs)


@method_decorator(associationDecorators, name='dispatch')
class EventsListViewForDraws(ListView):
    model = Event
    context_object_name = 'eventList'
    template_name = 'event-management-system/object-lists/eventListWithDrawsbtn.html'

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['states'] = State.objects.filter(stateID=1)
        return super(EventsListViewForDraws, self).get_context_data(**kwargs)


# List players on events as A list before shuffling.
@method_decorator(associationDecorators, name='dispatch')
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
            for asso in d.keys():
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


@login_required
@association_required
def delete_player(request, pk):
    query = Player.objects.get(pk=pk)
    query.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
@association_required
def delete_coach(request, pk):
    query = Coach.objects.get(pk=pk)
    query.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))