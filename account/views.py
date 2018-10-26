from django.contrib.auth import get_user_model, authenticate, login
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
    success_url = reverse_lazy('setup')
    template_name = 'registration/SignUp.html'
    def form_valid(self, form):
        valid = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid

    





class SetUp(CreateView):
    # form_class = forms.SetUpForm
    model = UserProfile
    fields = ('Phone',
            'nick_name',
            'Target_phone',
            'Type',
            'Status', )
    success_url = reverse_lazy('home')
    template_name = 'registration/SetUp.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.User = self.request.user
        self.object.Setup = True

        self.object.save()
        return super().form_valid(form)

    # def act(self):
    #     return activate.Setup()
