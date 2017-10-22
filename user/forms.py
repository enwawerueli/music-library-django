from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    username = forms.CharField(min_length=2, max_length=30)
    password = forms.CharField(min_length=8, widget=forms.PasswordInput)


class SignUpForm(forms.ModelForm):

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('This field is required')
        return email

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        if cleaned_data.get('password1') != cleaned_data.get('password2'):
            self.add_error('password2', forms.ValidationError('Your password do not match'))
        return cleaned_data

    password1 = forms.CharField(min_length=8, widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']
