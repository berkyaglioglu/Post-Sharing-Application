from django import forms
from .models import User


class RegisterationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RegisterationForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'gender', 'email', 'password']


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, required=True, widget=forms.TextInput())
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
