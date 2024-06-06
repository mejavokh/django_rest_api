from django.db import models
from django.utils.translation import gettext_lazy as _


class DeliveryAddresses(models.Model):
    city = models.CharField(_('City'), max_length=120)
    street = models.CharField(_('Street'), max_length=120)
    home_number = models.IntegerField()

    class Meta:
        verbose_name = _('Delivery address')
        verbose_name_plural = _('Delivery addresses')

    def __str__(self):
        return self.city


class Contacts(models.Model):
    phone_number = models.CharField(_('Phone number'), max_length=120)

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")


