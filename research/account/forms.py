from django import forms
from django.utils.translation import ugettext_lazy as _

class loginForm(forms.Form):
    username = forms.CharField(label=_("email"),
                               widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    passwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                       label=_("password"))

class signupForm(forms.Form):
    username = forms.CharField(label=_("name"),
                               widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    passwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                       label=_("password"))
    email = forms.CharField(label=_("email"),
                               widget=forms.TextInput(attrs={'placeholder': 'Email'}))
