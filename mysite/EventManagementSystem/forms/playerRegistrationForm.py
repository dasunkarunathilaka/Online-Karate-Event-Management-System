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

    district = forms.ModelChoiceField(queryset=District.objects.all())
    event = forms.ModelChoiceField(queryset=Event.objects.all())

    class Meta:
        model = Player
        fields = ('playerName', 'telephone', 'district', 'event')

    @transaction.atomic
    def save(self, commit=True):
        playerName = self.cleaned_data['playerName']
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
