from django.db import models
from accounts.models import Member

class EmailNotification(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    sent_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Notification for {self.member}"
