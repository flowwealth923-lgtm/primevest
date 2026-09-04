from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("user", "balance", "total_invested", "total_withdrawal", "referral_earnings")
    list_editable = ("balance", "total_invested", "total_withdrawal", "referral_earnings")
    search_fields = ("user__username", "user__email")