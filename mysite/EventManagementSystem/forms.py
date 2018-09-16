from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from models import User


class SlkfSignupForm(UserCreationForm):
    firstName = forms.CharField(required=True)
    lastName = forms.CharField(required=True)
    position = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.USER_TYPE_CHOICES = 'SL'
        user.save()
        # student = Student.objects.create(user=user)
        # student.interests.add(*self.cleaned_data.get('interests'))
        return user
