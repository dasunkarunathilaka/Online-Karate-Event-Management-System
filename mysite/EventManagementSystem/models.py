from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # New field needs to be added to the User table.

    # This gives a select box to the user to choose from. First parameter is the one stored in the database.
    USER_TYPE_CHOICES = (
        ('SL', 'SLKF'),
        ('AS', 'association'),
        ('DI', 'district'),
        ('PR', 'province'),
        ('AD', 'admin')
    )

    userType = models.CharField(max_length=2, choices=USER_TYPE_CHOICES, default='AD')

    def __unicode__(self):
        return self.username


class Slkf(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # memberName = models.CharField(max_length=100)

    # position in the SLKF
    position = models.CharField(max_length=50, blank=False)
    telephone = models.CharField(max_length=12, blank=False)

    def __unicode__(self):
        return self.user.username
        # user object will return according to its __unicode__ method (username)


class Association(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # Association does not need a unique ID because it can have username from User model.

    # associationID = models.CharField(max_length=100, blank=False, unique=True)
    associationName = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=1000, blank=False)
    telephone = models.CharField(max_length=12, blank=False)
    chiefInstructorName = models.CharField(max_length=100, blank=False)

    def __unicode__(self):
        return self.user.username


class Province(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # provinceName = models.CharField(max_length=50, blank=False)
    # Province Name is not needed - this is already in User table as the username.

    provinceSecretaryName = models.CharField(max_length=100, blank=False)
    telephone = models.CharField(max_length=12, blank=False)

    def __unicode__(self):
        return self.user.username


class District(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    # districtName = models.CharField(max_length=50, blank=False)
    # District Name is not needed - this is already in User table as the username.

    districtSecretaryName = models.CharField(max_length=100, blank=False)
    telephone = models.CharField(max_length=12, blank=False)

    # userType = models.CharField(max_length=2, choices=USER_TYPE_CHOICES, default='AD')

    def __unicode__(self):
        return self.user.username


class Event(models.Model):
    eventID = models.SmallIntegerField(primary_key=True)
    eventName = models.CharField(max_length=100, blank=False)

    # Weight, Age, Kata, Kumite.... details.

    def __unicode__(self):
        # return self.eventID
        # Cannot return an int. It must be a String or buffer - to show in html.
        return str(self.eventID)


class Player(models.Model):
    # Auto generated ID is the primary key.

    playerName = models.CharField(max_length=100, blank=False)
    telephone = models.CharField(max_length=12, blank=False)
    association = models.ForeignKey(Association, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    # players should be submitted to the system for each event he participates.
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __unicode__(self):
        return unicode(self.id)
