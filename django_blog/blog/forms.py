from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#registration form for new users
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", 'email', 'password1', 'password2')

#profile update form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture')

#email update form for profile view        
class UserEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)