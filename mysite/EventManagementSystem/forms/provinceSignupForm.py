from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from ..models import User, Province


class ProvinceSignupForm(UserCreationForm):

    provinceSecretaryName = forms.CharField(required=True, label="Province Secretary Name")
    telephone = forms.RegexField(regex=r'^(\+94)?1?\d{9}$', error_message=(
        "Phone number must be entered in the format: '+94769266301'. 11 digits allowed."))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'provinceSecretaryName', 'telephone', 'password1', 'password2')

    #     Province name is taken as the username.

    @transaction.atomic
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        password = self.cleaned_data['password1']
        user.set_password(password)
        # user.username = self.cleaned_data['provinceName']

        provinceSecretaryName = self.cleaned_data['provinceSecretaryName']
        telephone = self.cleaned_data['telephone']

        user.userType = 'PR'

        if commit:
            user.save()
            province = Province(user=user,
                                provinceSecretaryName=provinceSecretaryName,
                                telephone=telephone)
            province.save()
        return user
