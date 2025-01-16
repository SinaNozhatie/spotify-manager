from django import forms
from .models import SpotifyAccount, Member

class SpotifyAccountForm(forms.ModelForm):
    class Meta:
        model = SpotifyAccount
        fields = ['email', 'password', 'purchase_date', 'expiry_date']
        widgets = {
            'password': forms.PasswordInput(),
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'})
        }

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'spotify_account', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }
