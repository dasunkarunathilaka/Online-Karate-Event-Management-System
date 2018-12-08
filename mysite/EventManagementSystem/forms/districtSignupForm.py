from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from ..models import Province, User, District


class DistrictSignupForm(UserCreationForm):

    # Get province objects from the database.
    province = forms.ModelChoiceField(queryset=Province.objects.all())
    # In the drop down, the unicode function defined in Model class is called.
    # It returns the username of the Province, which is the provinceName.

    firstName = forms.CharField(required=True, label="District Secretary First Name")
    lastName = forms.CharField(required=True, label="District Secretary Last Name")

    # districtSecretaryName = forms.CharField(required=True, label="District Secretary Name")
    telephone = forms.RegexField(regex=r'^(\+94)?1?\d{9}$', error_message=(
        "Phone number must be entered in the format: '+94769266301'. 11 digits allowed."))
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'province', 'firstName', 'lastName', 'telephone', 'email', 'password1', 'password2')

    #     District name is taken as the username.

    @transaction.atomic
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        password = self.cleaned_data['password1']
        user.set_password(password)
        user.first_name = self.cleaned_data['firstName']
        user.last_name = self.cleaned_data['lastName']
        user.email = self.cleaned_data['email']

        # Province cannot use as a user attribute. It will try to create a
        # Province Object and raise an exception because District cannot be saved
        # without saving the related Province first.
        province = self.cleaned_data['province']
        districtSecretaryName = self.cleaned_data['firstName'] + " " + self.cleaned_data['lastName']
        telephone = self.cleaned_data['telephone']

        user.userType = 'DI'

        if commit:
            user.save()
            district = District(user=user,
                                province=province,
                                districtSecretaryName=districtSecretaryName,
                                telephone=telephone)
            district.save()
        return user
