from django.forms import ModelForm
from App_Login.models import User, Profile

from django.contrib.auth.forms import UserCreationForm


#first form
class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        exclude=('User',)

class SignUpForm(UserCreationForm):
    class Meta:
        model=User 
        fields=('email','password1','password2',)
        