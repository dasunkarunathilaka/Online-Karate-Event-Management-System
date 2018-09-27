from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from ..decorators import slkf_required
from ..models import User
from ..forms.provinceSignupForm import ProvinceSignupForm

decorators = [login_required, slkf_required]


@method_decorator(decorators, name='dispatch')
class ProvinceSignUpView(CreateView):
    model = User
    form_class = ProvinceSignupForm
    template_name = 'event-management-system/registration/provinceSignupForm.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Province'
        return super(ProvinceSignUpView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return HttpResponseRedirect('signup-success')
