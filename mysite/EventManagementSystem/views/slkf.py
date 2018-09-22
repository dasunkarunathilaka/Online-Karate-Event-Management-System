from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView

# This is a class based view. Instead of using a method as a view, this whole class can be used.
# as_view() method needs to be called (inherited from CreateView) in the urls.py
from ..decorators import slkf_required
from ..forms import SlkfSignupForm
from ..models import User


# Decorators are added to prevent unauthorized users getting these views via typing url in the browser.
@method_decorator(slkf_required, name='dispatch')
class SignUpDirectingView(TemplateView):
    template_name = 'event-management-system/signupDirect.html'


@method_decorator(slkf_required, name='dispatch')
class SlkfSignUpView(CreateView):
    model = User
    form_class = SlkfSignupForm
    template_name = 'event-management-system/registration/slkfSignupForm.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'SLKF'
        return super(SlkfSignUpView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return HttpResponseRedirect('signup-success')


@method_decorator(slkf_required, name='dispatch')
class slkfPortal(TemplateView):
    template_name = 'event-management-system/slkf/slkfPortal.html'
