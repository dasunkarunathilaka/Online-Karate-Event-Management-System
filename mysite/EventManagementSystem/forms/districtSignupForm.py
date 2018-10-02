from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from ..models import Province, User, District


class DistrictSignupForm(UserCreationForm):
    districtName = forms.CharField(required=True)
    # Ex: slkf-galle

    # Get province objects from the database.
    province = forms.ModelChoiceField(queryset=Province.objects.all())

    districtSecretaryName = forms.CharField(required=True)
    telephone = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('districtName', 'province', 'districtSecretaryName', 'telephone', 'password1', 'password2')

    #     District name is taken as the username.

    @transaction.atomic
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        password = self.cleaned_data['password1']
        user.set_password(password)
        user.username = self.cleaned_data['districtName']

        # Province cannot use as a user attribute. It will try to create a
        # Province Object and raise an exception because District cannot be saved
        # without saving the related Province first.
        province = self.cleaned_data['province']
        districtSecretaryName = self.cleaned_data['districtSecretaryName']
        telephone = self.cleaned_data['telephone']

        user.userType = 'DI'

        if commit:
            user.save()
            district = District(user=user, province=province, districtName=user.username,
                                districtSecretaryName=districtSecretaryName, telephone=telephone)
            district.save()
        return user
