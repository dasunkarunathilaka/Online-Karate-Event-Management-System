from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import CreateView

from ..models import User
from ..forms import ProvinceSignupForm


class ProvinceSignUpView(CreateView):
    model = User
    form_class = ProvinceSignupForm
    template_name = 'event-management-system/registration/provinceSignupForm.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'province'
        return super(ProvinceSignUpView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return HttpResponseRedirect('signup-success')