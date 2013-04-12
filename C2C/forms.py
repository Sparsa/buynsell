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

    def clean_phno(self):
        data = self.cleaned_data['phno']
        if len(str(data)) != 10:
            raise forms.ValidationError("Phone number must be of 10 digits!")

        return data

    def clean_password(self):
        pswd = self.cleaned_data.get('password')
        if len(str(pswd)) < 6:
            raise forms.ValidationError("The password must be atleast of 6 charecters")
        return pswd

    def get_password(self):
        return self.clean

    def clean_retype_password(self):
        pswd = self.cleaned_data.get('password')
        re_pswd = self.cleaned_data.get('retype_password')
        if str(pswd) != str(re_pswd):
            raise forms.ValidationError("The passwords doesn't match")
        return re_pswd



