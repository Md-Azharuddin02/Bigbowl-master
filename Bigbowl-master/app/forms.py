
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField , PasswordChangeForm, PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy  as _
from django.contrib.auth import password_validation

class CustomerRegistrationForm(UserCreationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class':'form-control' }))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email =forms.CharField(label='Email',required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model= User
        fields= ['username','email','password1','password2']
        labels= {'email':'Email'}
        Widgets= {'username':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}))
# ---------password change form------
class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=("Old Password"), strip=False, widget=forms.PasswordInput(attrs={ 'autocomplete':'current-password','autofocus':True,'class':'form-control',}))

    new_password1 = forms.CharField(label=("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),
    help_text=password_validation.password_validators_help_text_html())

    new_password2 = forms.CharField(label=("Confirm Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))

# ------------------forgot password form-------------

class ForgotPassword(PasswordResetForm):
    email =forms.EmailField(label='Email',max_length=254, required=True,widget=forms.EmailInput(attrs={'autocomplete':'email', 'class':'form-control','placeholder':'Enter your email id'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),
    help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=("Confirm Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
