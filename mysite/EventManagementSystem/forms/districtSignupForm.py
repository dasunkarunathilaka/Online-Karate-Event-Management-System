from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from ..models import Province, User, District


class DistrictSignupForm(UserCreationForm):
    districtName = forms.CharField(required=True)

    # Get province objects from the database.
    province = forms.ModelChoiceField(queryset=Province.objects.all())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('districtName', 'password1', 'password2', 'province')

    #     District name is taken as the username.

    @transaction.atomic
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        password = self.cleaned_data['password1']
        user.set_password(password)
        user.username = self.cleaned_data['districtName']

        # Province cannot user as a user attribute. It will try to create a
        # Province Object and raise an exception because District cannot be saved
        # without saving the related Province first.
        province = self.cleaned_data['province']

        user.userType = 'DI'

        if commit:
            user.save()
            district = District(user=user, province=province, districtName=user.username)
            district.save()
        return user