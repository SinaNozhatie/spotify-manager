from django.test import TestCase
from django.core.mail import send_mail

class EmailServiceTest(TestCase):
    def test_email_service(self):
        result = send_mail(
            'Test Email Service',
            'Automated test email',
            'postmaster@sandbox031ce7b234b94935b185325a0d670088.mailgun.org',
            ['sinmusic80@gmail.com'],
            fail_silently=False,
        )
        self.assertEqual(result, 1)
