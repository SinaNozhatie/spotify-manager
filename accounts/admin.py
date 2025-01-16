from django.contrib import admin
from .models import SpotifyAccount, Member

@admin.register(SpotifyAccount)
class SpotifyAccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'available_slots', 'purchase_date', 'expiry_date')
    search_fields = ('email',)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'spotify_account', 'start_date', 'end_date')
    search_fields = ('name', 'email')
