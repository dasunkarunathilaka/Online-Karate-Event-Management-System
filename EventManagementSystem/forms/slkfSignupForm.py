from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from EventManagementSystem.models import User, Slkf


class SlkfSignupForm(UserCreationForm):
    username = forms.CharField(required=True, label="Username")
    firstName = forms.CharField(required=True, label="First Name")
    lastName = forms.CharField(required=True, label="Last Name")
    position = forms.CharField(required=True, label="Position at SLKF")
    telephone = forms.RegexField(regex=r'^(\+94)?1?\d{9}$', error_messages={'invalid':
        "Phone number must be entered in the format: '+94769266301'. 11 digits allowed."})
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'firstName', 'lastName', 'position', 'telephone', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)

        password = self.cleaned_data['password1']
        user.set_password(password)

        user.username = self.cleaned_data['username']
        user.position = self.cleaned_data['position']
        user.first_name = self.cleaned_data['firstName']
        user.last_name = self.cleaned_data['lastName']
        user.userType = 'SL'
        user.email = self.cleaned_data['email']
        telephone = self.cleaned_data['telephone']

        if commit:
            user.save()
            slkf = Slkf(user=user, position=user.position, telephone=telephone)
            slkf.save()
        return user
