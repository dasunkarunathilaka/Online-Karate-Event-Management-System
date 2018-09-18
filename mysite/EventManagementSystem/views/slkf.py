from django.views.generic import CreateView, TemplateView

# This is a class based view. Instead of using a method as a view, this whole class can be used.
# as_view() method needs to be called (inherited from CreateView) in the urls.py
from ..forms import SlkfSignupForm
from ..models import User


class SignUpDirectingView(TemplateView):
    template_name = 'event-management-system/signupDirect.html'


class SlkfSignUpView(CreateView):
    model = User
    form_class = SlkfSignupForm
    template_name = 'event-management-system/registration/slkfSignupForm.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'SLKF'
        return super(SlkfSignUpView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()

        # print ("User Type --------------------" + user.USER_TYPE_CHOICES)
        # login(self.request, user)
        # return redirect('students:quiz_list')
