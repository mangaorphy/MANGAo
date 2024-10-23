from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'autoficus':'True',
        'class':'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'autocomplete':'current-password','class':'form-control'
    }))

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'autofocus': "True", "class":'forms-control'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class:':'forms-control'
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput (
        attrs={'class': 'form-control'}
    ))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class':'form-control'}
    ))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address', 'zip_code', 'country', 'region']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'zip_code', 'country', 'region']  # Include only address-related fields

        # Optional: Add widgets or custom styling
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your zip code'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'region': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your region'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional: Add placeholders or labels customization
        self.fields['address'].label = "Address"
        self.fields['zip_code'].label = "Zip Code"
        self.fields['country'].label = "Country"
        self.fields['region'].label = "Region"