from django.db import models
from django.contrib.auth.hashers import make_password


class SpotifyAccount(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    purchase_date = models.DateField()
    expiry_date = models.DateField()
    available_slots = models.IntegerField(default=5)
    
    class Meta:
            indexes = [
                models.Index(fields=['email']),
            ]    

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
    

class Member(models.Model):
    spotify_account = models.ForeignKey(SpotifyAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    start_date = models.DateField()
    end_date = models.DateField()
    
    def save(self, *args, **kwargs):
        if not self.pk:  # اگر عضو جدید است
            account = self.spotify_account
            if account.available_slots > 0:
                account.available_slots -= 1
                account.save()
            else:
                raise ValueError("No available slots!")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        account = self.spotify_account
        account.available_slots += 1
        account.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name


def fix_slots(self):
    total_members = self.member_set.count()
    self.available_slots = 5 - total_members
    self.save()

