from django import forms
from django.core import validators





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



class comments(forms.Form):
    pass