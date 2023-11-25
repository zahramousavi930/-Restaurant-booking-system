from django import forms
from django.core import validators
from .models import Comments
from django.forms import ModelForm




class Reservation(forms.Form):
    name =forms.CharField(
        widget=forms.TextInput(attrs={'placeholder' :'name' ,'class' :'form-control'}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    phone =forms.CharField(
        widget=forms.TextInput(attrs={'placeholder' :'phone' ,'class' :'form-control'}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    email = forms.EmailField(

        widget=forms.EmailInput(
            attrs={'placeholder': 'email', 'class': 'form-control',}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )






class comment_form(forms.Form):
    c_name= forms.CharField(
        widget=forms.TextInput(attrs={'placeholder' :'name' ,'class' :'form-control'}),
        validators=[
            validators.MaxLengthValidator(200)
        ]
    )

    c_email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'email', 'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(200),
            validators.EmailValidator()
        ]
    )

    c_text= forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'text', 'class': 'form-control' , 'row':'5'}),
        validators=[
            validators.MaxLengthValidator(200)
        ]
    )
