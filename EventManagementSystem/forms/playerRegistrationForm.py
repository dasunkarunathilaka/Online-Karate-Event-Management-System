from django.db import transaction
from django.forms import ModelForm
from django import forms

from ..models import Player, Association, District, Event


class PlayerRegistrationForm(ModelForm):

    # Constructor gets the user object passed by the view class.
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PlayerRegistrationForm, self).__init__(*args, **kwargs)

    # association = forms.ModelChoiceField(queryset=Association.objects.all())
    # This would allow Associations to submit players from other Associations.

    firstName = forms.CharField(required=True, label="Player First Name")
    lastName = forms.CharField(required=True, label="Player Last Name")
    district = forms.ModelChoiceField(queryset=District.objects.all())
    event = forms.ModelChoiceField(queryset=Event.objects.all())
    telephone = forms.RegexField(regex=r'^(\+94)?1?\d{9}$', error_messages={'invalid':
        "Phone number must be entered in the format: '+94769266301'. 11 digits allowed."})

    class Meta:
        model = Player
        fields = ('firstName', 'lastName', 'telephone', 'district', 'event')

    @transaction.atomic
    def save(self, commit=True):
        playerName = self.cleaned_data['firstName'] + " " + self.cleaned_data['lastName']
        telephone = self.cleaned_data['telephone']
        district = self.cleaned_data['district']
        event = self.cleaned_data['event']

        # Only the logged in user can submit its players.
        association = self.user.association

        if commit:
            player = Player(playerName=playerName,
                            telephone=telephone,
                            association=association,
                            district=district,
                            event=event,
                            )

            player.save()

        return player
