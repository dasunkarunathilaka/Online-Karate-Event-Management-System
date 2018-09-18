from django.views.generic import CreateView

from ..models import User
from ..forms import AssociationSignupForm


class AssociationSignUpView(CreateView):
    model = User
    form_class = AssociationSignupForm
    template_name = 'event-management-system/registration/associationSignupForm.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'association'
        return super(AssociationSignUpView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()