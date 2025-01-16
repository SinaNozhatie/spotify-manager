from rest_framework import serializers
from .models import SpotifyAccount, Member

class SpotifyAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyAccount
        fields = ['id', 'email', 'purchase_date', 'expiry_date', 'available_slots']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'name', 'email', 'spotify_account', 'start_date', 'end_date']
