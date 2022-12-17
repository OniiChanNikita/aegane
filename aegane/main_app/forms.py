from django import forms


class InputUserForm(forms.Form):
    username = forms.CharField();
    password = forms.CharField(widget=forms.PasswordInput);
