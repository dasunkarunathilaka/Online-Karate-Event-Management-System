from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView

from ..decorators import slkf_required
from ..models import User
from ..forms.associationSignupForm import AssociationSignupForm

decorators = [login_required, slkf_required]


@method_decorator(decorators, name='dispatch')
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


@method_decorator(decorators, name='dispatch')
class AssociationPortal(TemplateView):
    template_name = 'event-management-system/association/associationPortal.html'


@method_decorator(decorators, name='dispatch')
class PlayerRegistrationView(CreateView):
    # model = Player
    # form_class = PlayerRegistrationForm

    template_name = 'event-management-system/association/playerRegistrationForm.html'


@method_decorator(decorators, name='dispatch')
class CoachRegistrationView(CreateView):
    # model = Coach
    # form_class = CoachRegistrationForm

    template_name = 'event-management-system/association/coachRegistrationForm.html'
