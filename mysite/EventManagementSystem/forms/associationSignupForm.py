from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from ..models import User, Association


class AssociationSignupForm(UserCreationForm):
    # associationID = forms.RegexField(regex=r'^(slkf-)\d+$',
    #                                  error_message="Association ID must be entered in the format: slkf-12 (all lowercase)")
    # Ex: slkf-12

    # associationID = forms.CharField(required=True)

    username = forms.CharField(required=True, label="Registration ID (Username)")
    associationName = forms.CharField(required=True, label="Association Name")
    address = forms.CharField()
    telephone = forms.RegexField(regex=r'^(\+94)?1?\d{9}$', error_message=(
        "Phone number must be entered in the format: '+94769266301'. 11 digits allowed."))

    email = forms.EmailField(required=True, label="Association Email")
    chiefInstructorName = forms.CharField(required=True, label="Chief Instructor Name")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username', 'associationName', 'address', 'telephone', 'email', 'chiefInstructorName', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        password = self.cleaned_data['password1']
        user.set_password(password)
        user.username = self.cleaned_data['username']
        user.address = self.cleaned_data['address']
        user.telephone = self.cleaned_data['telephone']
        user.email = self.cleaned_data['email']

        associationName = self.cleaned_data['associationName']
        chiefInstructorName = self.cleaned_data['chiefInstructorName']

        user.userType = 'AS'

        if commit:
            user.save()
            association = Association(user=user,
                                      associationName=associationName,
                                      address=user.address,
                                      telephone=user.telephone,
                                      chiefInstructorName=chiefInstructorName
                                      )
            association.save()
        return user
