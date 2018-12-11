from django import forms
from django.db import transaction
from django.forms import ModelForm

from ..models import Event


class EventCreationForm(ModelForm):
    kumite = forms.RadioSelect()

    class Meta:
        model = Event
        fields = '__all__'

        # for a radio button
        # widgets = {
        #     'kumite': forms.RadioSelect
        # }
        # fields = ['eventID', 'eventName']

    @transaction.atomic
    def save(self, commit=True):
        eventID = self.cleaned_data['eventID']
        eventName = self.cleaned_data['eventName']
        kumite = self.cleaned_data['kumite']

        if commit:
            event = Event(eventID=eventID, eventName=eventName, kumite=kumite)
            event.save()
        return event
