from django import forms
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['user_name', 'e_mail', 'password']
