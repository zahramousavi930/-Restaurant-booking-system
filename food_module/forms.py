from django import forms
from django.core import validators
from .models import reservation





class ReservationForm(forms.ModelForm):
    class Meta:
        model = reservation
        fields = ['name', 'phone', 'email', 'number_of_guests']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'name','class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder':'phone','class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder':'email','class': 'form-control'}),
            'number_of_guests': forms.NumberInput(attrs={'placeholder':'number of guests','class': 'form-control'}),

        }





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
        widget=forms.Textarea(attrs={'placeholder': 'text', 'class': 'form-control' }),
        validators=[
            validators.MaxLengthValidator(200)
        ]
    )
