from django import forms
from django.db import transaction
from django.forms import ModelForm

from ..models import Coach


class CoachRegistrationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(CoachRegistrationForm, self).__init__(*args, **kwargs)

    telephone = forms.RegexField(regex=r'^(\+94)?1?\d{9}$', error_message=(
        "Phone number must be entered in the format: '+94769266301'. 11 digits allowed."))

    class Meta:
        model = Coach
        fields = ('coachID', 'coachName', 'telephone')

    @transaction.atomic
    def save(self, commit=True):
        coachID = self.cleaned_data['coachID']
        coachName = self.cleaned_data['coachName']
        telephone = self.cleaned_data['telephone']
        association = self.user.association

        if commit:
            coach = Coach(
                coachID=coachID,
                coachName=coachName,
                telephone=telephone,
                association=association,
            )

            coach.save()

        return coach
