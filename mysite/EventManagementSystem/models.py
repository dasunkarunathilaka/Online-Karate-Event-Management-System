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

    associationName = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=1000, blank=False)
    telephone = models.CharField(max_length=12, blank=False)

    def __unicode__(self):
        return self.user.username


class Province(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    provinceName = models.CharField(max_length=50, blank=False)
    provinceSecretaryName = models.CharField(max_length=100, blank=False)
    telephone = models.CharField(max_length=12, blank=False)

    def __unicode__(self):
        return self.user.username


class District(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    districtName = models.CharField(max_length=50, blank=False)
    districtSecretaryName = models.CharField(max_length=100, blank=False)
    telephone = models.CharField(max_length=12, blank=False)

    # userType = models.CharField(max_length=2, choices=USER_TYPE_CHOICES, default='AD')

    def __unicode__(self):
        return self.user


class Event(models.Model):
    eventID = models.SmallIntegerField(primary_key=True)
    eventName = models.CharField(max_length=100, blank=False)
    # Weight, Age, Kata, Kumite.... details.
