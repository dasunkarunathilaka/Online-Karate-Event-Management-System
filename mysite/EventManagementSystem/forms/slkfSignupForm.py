from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from ..models import User, Slkf


class SlkfSignupForm(UserCreationForm):
    firstName = forms.CharField(required=True)
    lastName = forms.CharField(required=True)
    position = forms.CharField(required=True)
    telephone = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'firstName', 'lastName', 'position', 'telephone', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        password = self.cleaned_data['password1']
        user.set_password(password)

        user.position = self.cleaned_data['position']
        user.first_name = self.cleaned_data['firstName']
        user.last_name = self.cleaned_data['lastName']
        user.userType = 'SL'
        telephone = self.cleaned_data['telephone']

        if commit:
            user.save()
            slkf = Slkf(user=user, position=user.position, telephone=telephone)
            slkf.save()
        return user
