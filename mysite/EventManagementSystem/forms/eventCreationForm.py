from django.db import transaction
from django.forms import ModelForm

from ..models import Event


class EventCreationForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        # fields = ['eventID', 'eventName']

    @transaction.atomic
    def save(self, commit=True):
        eventID = self.cleaned_data['eventID']
        eventName = self.cleaned_data['eventName']

        if commit:
            event = Event(eventID=eventID, eventName=eventName)
            event.save()
        return event
