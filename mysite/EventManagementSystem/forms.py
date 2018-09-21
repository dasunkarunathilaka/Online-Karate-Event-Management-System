from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from models import User, Slkf, Association, District, Province


class SlkfSignupForm(UserCreationForm):
    firstName = forms.CharField(required=True)
    lastName = forms.CharField(required=True)
    position = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'firstName', 'lastName', 'position', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        password = self.cleaned_data['password1']
        user.set_password(password)

        user.position = self.cleaned_data['position']
        user.first_name = self.cleaned_data['firstName']
        user.last_name = self.cleaned_data['lastName']
        user.userType = 'SL'

        if commit:
            user.save()
            slkf = Slkf(user=user, position=user.position)
            slkf.save()
        return user


class AssociationSignupForm(UserCreationForm):
    associationID = forms.CharField(required=True)
    associationName = forms.CharField(required=True)
    address = forms.CharField()
    telephone = forms.RegexField(regex=r'^\+?1?\d{11}$', error_message=(
        "Phone number must be entered in the format: '+999999999'. 11 digits allowed."))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('associationID', 'associationName', 'address', 'telephone', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        password = self.cleaned_data['password1']
        user.set_password(password)
        user.username = self.cleaned_data['associationID']
        user.address = self.cleaned_data['address']
        user.telephone = self.cleaned_data['telephone']

        user.userType = 'AS'

        if commit:
            user.save()
            association = Association(user=user, associationName=user.username, address=user.address,
                                      telephone=user.telephone)
            association.save()
        return user


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


class DistrictSignupForm(UserCreationForm):
    districtName = forms.CharField(required=True)

    # province = forms.

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('districtName', 'password1', 'password2')

    #     District name is taken as the username.

    @transaction.atomic
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        password = self.cleaned_data['password1']
        user.set_password(password)
        user.username = self.cleaned_data['districtName']

        user.userType = 'DI'

        if commit:
            user.save()
            # district = District(user=user, associationName=user.username, address=user.address,
            #                           telephone=user.telephone)
            # district.save()
        return user
