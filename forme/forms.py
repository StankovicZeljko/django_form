# form/forms.py
from django import forms
from django.core.validators import RegexValidator
from .models import PotentialUserInformation

# Define regex for postal codes and phone numbers
postal_code_regex = RegexValidator(
    regex=r'^\d{4,5}$',
    message='Enter a valid postal code.'
)
phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message='Enter a valid phone number.'
)

class PotentialUserInformationForm(forms.ModelForm):
    class Meta:
        model = PotentialUserInformation
        fields = [
            'gender', 'first_name', 'last_name', 'email', 'organization',
            'country', 'street', 'postal_code', 'city', 'phone'
        ]
        widgets = {
            'gender': forms.RadioSelect(),
            'country': forms.Select(),
        }

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    organization = forms.CharField(required=True)
    street = forms.CharField(required=True)
    postal_code = forms.CharField(required=True, validators=[postal_code_regex])
    city = forms.CharField(required=True)
    phone = forms.CharField(required=True, validators=[phone_regex])
