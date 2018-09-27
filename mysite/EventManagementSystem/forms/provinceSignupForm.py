from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from ..models import User, Province


class ProvinceSignupForm(UserCreationForm):
    provinceName = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('provinceName', 'password1', 'password2')

    #     Province name is taken as the username.

    @transaction.atomic
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        password = self.cleaned_data['password1']
        user.set_password(password)
        user.username = self.cleaned_data['provinceName']

        user.userType = 'PR'

        if commit:
            user.save()
            province = Province(user=user, provinceName=user.username)
            province.save()
        return user