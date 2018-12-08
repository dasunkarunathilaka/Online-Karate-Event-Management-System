from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from ..models import User, Province


class ProvinceSignupForm(UserCreationForm):
    firstName = forms.CharField(required=True, label="District Secretary First Name")
    lastName = forms.CharField(required=True, label="District Secretary Last Name")
    telephone = forms.RegexField(regex=r'^(\+94)?1?\d{9}$', error_message=(
        "Phone number must be entered in the format: '+94769266301'. 11 digits allowed."))

    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'firstName', 'lastName', 'telephone', 'email', 'password1', 'password2')

    #     Province name is taken as the username.

    @transaction.atomic
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        password = self.cleaned_data['password1']
        user.set_password(password)
        user.first_name = self.cleaned_data['firstName']
        user.last_name = self.cleaned_data['lastName']
        user.email = self.cleaned_data['email']

        provinceSecretaryName = self.cleaned_data['firstName'] + " " + self.cleaned_data['lastName']
        telephone = self.cleaned_data['telephone']

        user.userType = 'PR'

        if commit:
            user.save()
            province = Province(user=user,
                                provinceSecretaryName=provinceSecretaryName,
                                telephone=telephone)
            province.save()
        return user
