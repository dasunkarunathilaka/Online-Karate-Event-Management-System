from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, ListView

from EventManagementSystem.decorators import slkf_required, province_required
from EventManagementSystem.models import User, Player, Coach, Event
from EventManagementSystem.forms.provinceSignupForm import ProvinceSignupForm

slkfDecorators = [login_required, slkf_required]
provinceDecorators = [login_required, province_required]


@method_decorator(slkfDecorators, name='dispatch')
class ProvinceSignUpView(CreateView):
    model = User
    form_class = ProvinceSignupForm
    template_name = 'event-management-system/registration/userCreationForm.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Province'
        return super(ProvinceSignUpView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'New province user created successfully!')
        return HttpResponseRedirect(reverse_lazy('province-users'))


@method_decorator(provinceDecorators, name='dispatch')
class ProvincePortal(TemplateView):
    template_name = 'event-management-system/province/provincePortal.html'


@method_decorator(provinceDecorators, name='dispatch')
class ProvincePlayersListView(ListView):
    model = Player
    context_object_name = 'playerList'
    template_name = 'event-management-system/object-lists/playerList.html'

    def get_queryset(self):
        queryset = Player.objects.filter(district__province__user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['province'] = self.request.user.username
        return super(ProvincePlayersListView, self).get_context_data(**kwargs)


@method_decorator(provinceDecorators, name='dispatch')
class ProvinceCoachesListView(ListView):
    model = Coach
    context_object_name = 'coachList'
    template_name = 'event-management-system/object-lists/coachList.html'

    def get_queryset(self):
        queryset = Coach.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['institute'] = self.request.user.username
        return super(ProvinceCoachesListView, self).get_context_data(**kwargs)


@method_decorator(provinceDecorators, name='dispatch')
class ProvinceEventsListView(ListView):
    model = Event
    context_object_name = 'eventList'
    template_name = 'event-management-system/object-lists/eventListWithPlayersbtn.html'

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset


@method_decorator(provinceDecorators, name='dispatch')
class ProvincePlayersByEventListView(ListView):
    model = Player
    context_object_name = 'playerList'
    template_name = 'event-management-system/object-lists/playerList.html'

    def get_queryset(self):
        queryset = Player.objects.filter(event__eventID=self.request.GET.get('event', ""),
                                         district__province__user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['event'] = self.request.GET.get('event', "")
        return super(ProvincePlayersByEventListView, self).get_context_data(**kwargs)
