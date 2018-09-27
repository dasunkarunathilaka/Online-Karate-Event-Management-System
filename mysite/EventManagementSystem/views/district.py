from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from ..decorators import slkf_required
from ..models import User
from ..forms.districtSignupForm import DistrictSignupForm

decorators = [login_required, slkf_required]


@method_decorator(decorators, name='dispatch')
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
