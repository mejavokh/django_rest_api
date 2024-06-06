from django.contrib import admin

from .models import *


@admin.register(DeliveryAddresses)
class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ['city', 'street', 'home_number']


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['phone_number',]



