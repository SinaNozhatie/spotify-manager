from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from .models import Member

@shared_task
def send_expiration_notifications():
    # اعضایی که 7 روز تا پایان اشتراکشان مانده
    soon_to_expire = Member.objects.filter(
        end_date=timezone.now().date() + timedelta(days=7),
        notification_sent=False
    )
    
    for member in soon_to_expire:
        send_mail(
            'Spotify Subscription Expiring Soon',
            f'Dear {member.name},\nYour subscription will expire in 7 days.',
            'from@example.com',
            [member.email],
            fail_silently=False,
        )
        member.notification_sent = True
        member.save()
