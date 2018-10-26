from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import auth
from django.db import models


users = get_user_model()

class User(auth.models.User, auth.models.PermissionsMixin):


    def __str__(self):
        return "@{}".format(self.username)



# One time setup

class UserProfile(models.Model):

    a_type_choice= (
            ('Sn','Single'),
            # ('Biz','Business'),
            ('Fm', 'Family'),
        )
    status_choice= (
            ('Sn','Single'),
            ('Ac','Active'),
            ('En', 'Engaged'),
            ('mr', 'Married'),
        )
    goal_choice= (

            ('Ac','Active'),
            ('Fr', 'Fairytale'),
            ('Pl', 'player'),
        )
    User = models.ForeignKey(users, related_name="User", on_delete='cascade')
    nick_name = models.CharField(max_length=8, verbose_name='Nickname')
    Phone = models.CharField(max_length=11, unique=True, validators=[RegexValidator(regex='^\d{11}$', message='invalid number', code='Invalid number')])
    Target_phone = models.CharField(max_length=11, unique=True, verbose_name="spouse number",validators=[RegexValidator(regex='^\d{11}$', message='invalid number', code='Invalid number')])
    Type = models.CharField(choices=a_type_choice, max_length=12)
    Status = models.CharField(choices=status_choice, verbose_name="Relationship status", max_length=12,)
    Goal = models.CharField(choices=goal_choice, max_length=12, null=True, blank=True)
    Setup = models.BooleanField(default=False)

    def __str__(self):
        return str(self.User)



    # SMS, VOICE,
