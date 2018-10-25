# Create your tasks here
from __future__ import absolute_import, unicode_literals
from account.models import UserProfile
from django.shortcuts import redirect
from celery import shared_task
from decouple import config
from . models import *
import requests



@shared_task
def SmsClient():
    Client = UserProfile.objects.all()

    for captain in Client:
        if captain.Setup:
            print(captain.Setup)
            if captain.Type == "Sn":
                print(captain.Type)
                SMS = sms.objects.all().order_by('?')[:1]

                for SMS2 in SMS:
                    if SMS2.genre == "si":
                        print(SMS2.message)
                        print(captain.User)
                        print(captain.Target_phone)

                client = requests.post('http://customer.smsprovider.com.ng/api/', data= {'username':config('username'),
                                                                                        'password':config('password'),
                                                                                        'message':SMS2.message,
                                                                                        'sender':captain.nick_name,
                                                                                        'mobiles':captain.Target_phone,})
                log = simple_log(user=captain.User, message=client.status_code)  #use this if you are on Heroku free plan or feel too lazy to implement a proper logger
                log.save()

            elif captain.Type == "Fm":
                print(captain.Type)
                SMS = sms.objects.all().order_by('?')[:1]
                for SMS3 in SMS:
                    if SMS3.genre == "fm":
                        print(SMS3.message)
                        print(str(captain.User))
                        print(captain.Target_phone)
                client = requests.post('http://customer.smsprovider.com.ng/api/', data= {'username':config('username'),
                                                                                        'password':config('password'),
                                                                                        'message':SMS3.message,
                                                                                        'sender':captain.nick_name,
                                                                                        'mobiles':captain.Target_phone,})
                log = simple_log(user=captain.User, message=client.status_code)  #use this if you are on Heroku free plan or feel too lazy to implement a proper logger
                log.save()




def VoiceClient():
    pass
