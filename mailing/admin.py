from django.contrib import admin
from mailing.models import Client, Mailing, Message, MailingAttempt
# Register your models here.
@admin.register(Client)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")


@admin.register(Mailing)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "status")


@admin.register(Message)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("id", "subject")
