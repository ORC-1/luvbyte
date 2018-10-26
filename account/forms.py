from django import forms
from . models import UserProfile, User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username',
                  'email',
                  'password1',)
        model = get_user_model()


        # password2 = forms.CharField(label=_("Whatever"), widget=MyPasswordInput

        # help_texts = {
        #     'username': None,
        #     'email': None,
        #     'password1':"Easy",
        #     'password2': None
        # }

        # # totally optional and can be replaced in front-end form call
        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     sel.fields['username'].label = 'Display Name'
        #     self.fields['email'].label = "Email Address"
            

# class SetUpForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         exclude = ('User', 'Setup')
