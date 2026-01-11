from django.conf import settings
from django.db import models

class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="account")

    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_invested = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_withdrawal = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    referral_earnings = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.user.username