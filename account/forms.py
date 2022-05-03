from socket import forms


class LoginForm(forms.Form):
    """
    This is a class to authenticate -
    users on response.
    """
    username = forms.Charfield()
    # PasswordInput used to render password input on html.
    # ex: <input type="password">
    password = forms.Charfield(widget=forms.PasswordInput)
