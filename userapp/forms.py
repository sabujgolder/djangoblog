from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class userreg(UserCreationForm):

    Email = forms.EmailField()

    class Meta:
        model=User
        fields=('username','Email','password1','password2')
