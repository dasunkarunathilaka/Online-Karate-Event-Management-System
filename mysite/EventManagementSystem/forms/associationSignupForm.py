from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from ..models import User, Association


class AssociationSignupForm(UserCreationForm):
    associationID = forms.RegexField(regex=r'^(slkf-)\d+$',
                                     error_message="Association ID must be entered in the format: slkf-12 (all lowercase)")
    # Ex: slkf-12

    # associationID = forms.CharField(required=True)

    associationName = forms.CharField(required=True)
    address = forms.CharField()
    telephone = forms.RegexField(regex=r'^(\+94)?1?\d{9}$', error_message=(
        "Phone number must be entered in the format: '+94769266301'. 11 digits allowed."))

    chiefInstructorName = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'associationID', 'associationName', 'address', 'telephone', 'chiefInstructorName', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        password = self.cleaned_data['password1']
        user.set_password(password)
        user.username = self.cleaned_data['associationID']
        user.address = self.cleaned_data['address']
        user.telephone = self.cleaned_data['telephone']
        associationName = self.cleaned_data['associationName']
        chiefInstructorName = self.cleaned_data['chiefInstructorName']

        user.userType = 'AS'

        if commit:
            user.save()
            association = Association(user=user,
                                      associationID=user.username,
                                      associationName=associationName,
                                      address=user.address,
                                      telephone=user.telephone,
                                      chiefInstructorName=chiefInstructorName
                                      )
            association.save()
        return user
