from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, ListView

from ..forms.coachRegistrationForm import CoachRegistrationForm
from ..forms.playerRegistrationForm import PlayerRegistrationForm
from ..decorators import slkf_required, association_required
from ..models import User, Event, Player, Coach
from ..forms.associationSignupForm import AssociationSignupForm

slkfDecorators = [login_required, slkf_required]
associationDecorators = [login_required, association_required]


@method_decorator(slkfDecorators, name='dispatch')
class AssociationSignUpView(CreateView):
    model = User
    form_class = AssociationSignupForm
    template_name = 'event-management-system/registration/associationSignupForm.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Association'
        return super(AssociationSignUpView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return HttpResponseRedirect('signup-success')


@method_decorator(associationDecorators, name='dispatch')
class AssociationPortal(TemplateView):
    template_name = 'event-management-system/association/associationPortal.html'


@method_decorator(associationDecorators, name='dispatch')
class PlayerRegistrationView(CreateView):
    model = Player
    form_class = PlayerRegistrationForm
    template_name = 'event-management-system/association/playerRegistrationForm.html'

    # Need to pass the currently logged in user to player registration form.
    # Player registration form have the Association column filled automatically.
    def get_form_kwargs(self):
        kwargs = super(PlayerRegistrationView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('player-registered')


@method_decorator(associationDecorators, name='dispatch')
class RegisteredPlayerListView(ListView):
    model = Player
    context_object_name = 'playerList'
    template_name = 'event-management-system/association/playerList.html'

    def get_queryset(self):
        queryset = Player.objects.filter(association=self.request.user.association)
        return queryset


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
        return HttpResponseRedirect('coach-registered')


@method_decorator(associationDecorators, name='dispatch')
class RegisteredCoachListView(ListView):
    model = Coach
    context_object_name = 'coachList'
    template_name = 'event-management-system/association/coachList.html'

    def get_queryset(self):
        queryset = Coach.objects.filter(association=self.request.user.association)
        return queryset
