from django.core.mail import send_mail
from .models import EmailLog

def send_notification_email(subject, message, recipient):
    try:
        send_mail(
            subject,
            message,
            'postmaster@sandbox031ce7b234b94935b185325a0d670088.mailgun.org',
            [recipient],
            fail_silently=False,
        )
        EmailLog.objects.create(
            recipient=recipient,
            subject=subject,
            status=True
        )
        return True
    except Exception as e:
        EmailLog.objects.create(
            recipient=recipient,
            subject=subject,
            status=False,
            error_message=str(e)
        )
        return False
