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
    )

    def __unicode__(self):
        return self.username


class Slkf(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    memberName = models.CharField(max_length=100)

    # position in the SLKF
    position = models.CharField(max_length=50)
    telephone = models.CharField(max_length=10)

    def __unicode__(self):
        return self.user
        # user object will return according to its __unicode__ method (username)


class Association(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # Association does not need a unique ID because it can have username from User model.

    associationName = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    telephone = models.CharField(max_length=10)

    def __unicode__(self):
        return self.user


class Province(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    provinceName = models.CharField(max_length=50)

    def __unicode__(self):
        return self.user


class District(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    DistrictName = models.CharField(max_length=50)

    def __unicode__(self):
        return self.user
