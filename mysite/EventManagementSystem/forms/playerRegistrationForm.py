from django.db import transaction
from django.forms import ModelForm
from django import forms

from ..models import Player, Association, District, Event


class PlayerRegistrationForm(ModelForm):
    association = forms.ModelChoiceField(queryset=Association.objects.all())
    district = forms.ModelChoiceField(queryset=District.objects.all())
    event = forms.ModelChoiceField(queryset=Event.objects.all())

    class Meta:
        model = Player
        fields = '__all__'

    @transaction.atomic
    def save(self, commit=True):
        playerName = self.cleaned_data['playerName']
        telephone = self.cleaned_data['telephone']
        association = self.cleaned_data['association']
        district = self.cleaned_data['district']
        event = self.cleaned_data['event']

        if commit:
            player = Player(playerName=playerName,
                            telephone=telephone,
                            association=association,
                            district=district,
                            event=event,
                            )

            player.save()

        return player
