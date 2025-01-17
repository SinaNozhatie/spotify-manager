from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail
from accounts.models import Member
from datetime import timedelta

class Command(BaseCommand):
    help = 'Send notification emails to members expiring in 7 days'

    def handle(self, *args, **options):
        expiry_date = timezone.now().date() + timedelta(days=7)
        members = Member.objects.filter(expiry_date=expiry_date)
        
        for member in members:
            send_mail(
                'Spotify Membership Expiring Soon',
                f'Your membership will expire in 7 days on {member.expiry_date}',
                'from@example.com',
                [member.email],
                fail_silently=False,
            )
