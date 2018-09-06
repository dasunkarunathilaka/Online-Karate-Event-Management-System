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


# No need for a SLKF table as there is only one of them.
# Other users need to have tables because there are multiple instances of them.

class Association(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # Association does not need a unique ID because it can have username from User model.

    associationName = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    telephone = models.IntegerField(max_length=10)