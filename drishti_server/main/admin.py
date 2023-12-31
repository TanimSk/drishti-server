from django.contrib import admin
from .models import PreOrder


@admin.register(PreOrder)
class PreOrderAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "product",
        "quantity",
        "phone_number",
        "email_address",
        "address",
        "comment",
    )
