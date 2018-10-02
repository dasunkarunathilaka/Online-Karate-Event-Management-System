from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from ..models import User, Association


class AssociationSignupForm(UserCreationForm):
    # associationID = forms.RegexField(regex=r'^(SLKF-)\d$',
    #                                  error_message="Association ID must be entered in the format: SLKF-12")

    associationID = forms.CharField(required=True)
    # Ex: slkf-12

    associationName = forms.CharField(required=True)
    address = forms.CharField()
    telephone = forms.RegexField(regex=r'^(\+94)?1?\d{9}$', error_message=(
        "Phone number must be entered in the format: '+94769266301'. 11 digits allowed."))

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
