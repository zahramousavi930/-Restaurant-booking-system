from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

class RegisterForm(forms.Form):

    username=forms.CharField(
        label='username',
        widget=forms.TextInput(attrs={'placeholder':'enter username','class':'form-control validate','id':'r_username'})
    )



    email= forms.EmailField(
        label='email',
        widget=forms.EmailInput(attrs={'placeholder':'enter email','class':'form-control validate','id':'r_email'}),
        validators=[
            validators.MaxLengthValidator(200),
            validators.EmailValidator
        ]

    )
    password=forms.CharField(
        label='password',
        widget=forms.PasswordInput(attrs={'placeholder':'password','class':'form-control validate','id':'r_password'}),

    )




class LoginForm(forms.Form):
    email_or_username= forms.CharField(
        label='username or email',
        widget=forms.TextInput(attrs={'placeholder':'username / email','class':'form-control validate my-1' ,'id':'email_username'}),

    )
    password = forms.CharField(
        label=' password',
        widget=forms.PasswordInput(attrs={'placeholder':'enter password','class':'form-control validate my-1', 'id':'l_password' }),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )




class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(attrs={'placeholder':'enter email','class':'form-control forget'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label=' password',
        widget=forms.PasswordInput(attrs={'placeholder':'enter new password','class':'form-control'}),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )










