__author__ = 'sparsa'
from django import forms

'''Creating a Registration Form using forms.Form'''


class RegistrationForm(forms.Form):
    First_Name = forms.CharField(max_length=50)
    Last_Name = forms.CharField(max_length=50)
    phno = forms.IntegerField()
    email = forms.EmailField(max_length=50)
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))
    retype_password = forms.CharField(widget=forms.PasswordInput(render_value=False))




