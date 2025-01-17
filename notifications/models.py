from django.db import models
from accounts.models import Member

class EmailNotification(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    sent_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Notification for {self.member}"

class EmailLog(models.Model):
    sent_at = models.DateTimeField(auto_now_add=True)
    recipient = models.EmailField()
    subject = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.subject} to {self.recipient} - {'Success' if self.status else 'Failed'}"

