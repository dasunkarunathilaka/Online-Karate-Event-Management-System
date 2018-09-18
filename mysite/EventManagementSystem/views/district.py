from django.views.generic import CreateView

from ..models import User
from ..forms import DistrictSignupForm


class DistrictSignUpView(CreateView):
    model = User
    form_class = DistrictSignupForm
    template_name = 'event-management-system/registration/districtSignupForm.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'district'
        return super(DistrictSignUpView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()