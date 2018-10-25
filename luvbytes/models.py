from django.db import models
from django.contrib.auth import get_user_model





class sms(models.Model):
    sms_type =(('fm','family'),
                ('si','single'), )
    # User = get_user_model()
    # owner = models.ForeignKey(User, related_name="smsowner", on_delete='cascade')
    name = models.CharField(max_length=10, unique=True, )
    message = models.TextField(max_length=160, unique=True,)
    added_on = models.DateTimeField(auto_now=True)
    genre = models.CharField(choices=sms_type, max_length=12)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "sms"



class voice(models.Model):
    pass


class video(models.Model):
    pass


class tips(models.Model):
    Users = get_user_model()
    tip_choices =(('fm','family'),
                ('sx','sex'), )
    owner = models.ForeignKey(Users, related_name="tipowner", on_delete='cascade')
    type = models.CharField(choices=tip_choices, max_length=12)
    name = models.CharField(max_length=10, unique=True, )
    message = models.TextField(max_length=160, unique=True,)
    added_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class simple_log(models.Model):
    user = models.CharField(max_length= 200)
    message = models.TextField(max_length= 200)

    def __str__(self):
        return self.user
