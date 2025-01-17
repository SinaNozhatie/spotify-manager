from django.core.management.base import BaseCommand
from django.utils import timezone
from accounts.models import Member
from notifications.services import send_notification_email
from datetime import timedelta

class Command(BaseCommand):
    help = 'Send notification emails to members expiring in 7 days'

    def handle(self, *args, **options):
        expiry_date = timezone.now().date() + timedelta(days=7)
        members = Member.objects.filter(expiry_date=expiry_date)
        
        for member in members:
            subject = 'اشتراک Spotify شما رو به پایان است'
            message = f'سلام {member.name}،\n\nاشتراک Spotify شما در تاریخ {member.expiry_date} به پایان می‌رسد.'
            send_notification_email(subject, message, member.email)
