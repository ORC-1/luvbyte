from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.shortcuts import render
from . models import *
from . import forms

# Create your views here.

User = get_user_model()

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = redirect('setup')
    template_name = 'registration/SignUp.html'



class SetUp(CreateView):
    # form_class = forms.SetUpForm
    model = UserProfile
    fields = ('Phone',
            'nick_name',
            'Target_phone',
            'Type',
            'Status', )
    success_url = redirect('home')
    template_name = 'registration/SetUp.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.User = self.request.user
        self.object.Setup = True
        self.object.save()
        return super().form_valid(form)

    # def act(self):
    #     return activate.Setup()
