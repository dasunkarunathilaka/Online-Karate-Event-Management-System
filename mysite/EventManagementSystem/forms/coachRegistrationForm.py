from django.db import transaction
from django.forms import ModelForm
from ..models import Coach


class CoachRegistrationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(CoachRegistrationForm, self).__init__(*args, **kwargs)

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
