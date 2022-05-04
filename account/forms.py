from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    """
    This is a class to authenticate -
    users on response.
    """
    username = forms.CharField()
    # PasswordInput used to render password input on html.
    # ex: <input type="password">
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        # clean_<fieldname> is similar to resolve_<fieldname> of -
        # django-graphene as well as get_<fieldname> of DRF.
        # In other words, field validation.
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')

