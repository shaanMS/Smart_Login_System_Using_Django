from django import forms
from django.contrib.auth.models import User

class EmailSignupForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered")
        return email








class SetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
            raise forms.ValidationError("Passwords do not match")





class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)




class PersonalDetailsForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    dob = forms.DateField()
    aadhaar = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    address = forms.CharField(widget=forms.Textarea)
