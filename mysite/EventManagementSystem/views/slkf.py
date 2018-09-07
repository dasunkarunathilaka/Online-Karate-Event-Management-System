from django.views.generic import CreateView


# This is a class based view. Instead of using a method as a view, this whole class can be used.
# as_view() method needs to be called (inherited from CreateView) in the urls.py
class SignUpDirectingView(CreateView):
    pass


class SlkfSignUpView(CreateView):
    pass