from django import forms
from .models import User


class Register(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Register, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'gender', 'email', 'password']


class LoginForm(forms.Form):
    email = forms.CharField(max_length=50, required=True, widget=forms.TextInput())
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
