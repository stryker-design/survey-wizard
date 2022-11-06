import email
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, UserChangeForm
from django.contrib.auth.models import User 
from crispy_forms.helper import FormHelper

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
            super(UserCreationForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_show_labels = False 

            for fieldname in ['username', 'password1', 'password2']:
                self.fields[fieldname].help_text = None
                

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ManageAccountForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
            super(UserChangeForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_show_labels = False 

            for fieldname in ['username', 'email']:
                self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('username', 'email')


