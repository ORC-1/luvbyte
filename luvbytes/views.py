import requests
from . models import *
from random import randint
from celery import shared_task
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from account.models import UserProfile
from django.views.generic import ListView
from django.contrib.auth import authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)



# Home page view
@login_required
def home(request):
    username_log = request.user.username
    user_id = request.user.pk
    # status_check = UserProfile.objects.get(User=int(user_id))
    # if status_check.Setup: #check if user account setup is True
    #     return render(request, 'dashboard/home.html')
    # else:
    #     return redirect('setup')


    try:
        status_check = UserProfile.objects.get(User=int(user_id))
        if status_check.Setup: #check if user account setup is True
            return render(request, 'dashboard/home.html')
        else:
            return redirect('setup')

    except Exception as error:
        print(error)
        log = simple_log(user=username_log, message=error)  #use this if you are on Heroku free plan or feel too lazy to implement a proper logger
        log.save()
        return render(request, 'dashboard/error.html')



def signout(request):
    logout(request)
    return redirect('home')
