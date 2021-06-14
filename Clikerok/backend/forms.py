from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm,forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
#    def __init__(self, *args, **kwargs):
#        supper().__init__(self, *args, **kwargs)
#        for field in self.fields:
#            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
