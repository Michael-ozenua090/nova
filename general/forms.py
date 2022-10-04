from django import forms
from django.forms import ModelForm
from general.models import CustomUser
from django.contrib.auth.hashers import make_password


class CustomUserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    widget = {
            'password': forms.PasswordInput(),
        }
    class Meta:
        model = CustomUser
        fields = ('image', 'email', 'last_name', 'first_name', 'number', 'user_type',  'password')

    def clean_password(self):
        password = self.cleaned_data.get("password",None)
        if self.instance.pk is not None:
            if not password:
                return self.instance.password

        return make_password(password)
        