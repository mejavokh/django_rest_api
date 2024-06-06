from django.db import models

from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Media(models.Model):
    class FileType(models.TextChoices):
        IMAGE = 'image', _('Image')
        VIDEO = 'video', _('Video')

    file = models.FileField(upload_to='only_medias/',
                            verbose_name=_('File'),
                            validators=[FileExtensionValidator(allowed_extensions=[
                                'jpg', 'jpeg', 'png', 'webp',
                                'mp4', 'avi', 'mpeg4', 'mkv'
                            ])])
    file_type = models.CharField(max_length=10,
                                 verbose_name=_('File Type'),
                                 choices=FileType.choices)

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Media")

    def __str__(self):
        return f"Id: {self.id}|Name: {self.file.name.split('/')[-1]}"

    def clean(self):
        if self.file_type not in self.FileType.values:
            raise ValidationError(_('Invalid file type'))
        elif self.file_type == self.FileType.IMAGE:
            if self.file.name.split('.')[-1] not in ['jpg', 'jpeg', 'png', 'webp']:
                raise ValidationError(_('Invalid Image File'))
        elif self.file_type == self.FileType.VIDEO:
            if self.file.name.split('.')[-1] not in ['jpg', 'jpeg', 'png', 'webp']:
                raise ValidationError(_('Invalid Video File'))


class CommonSettings(models.Model):
    main_phone_number = models.CharField(max_length=20,
                                         verbose_name=_("Main Phone Number"))
    flowers_text = models.TextField(verbose_name=_("Flower Text"))
    service_page_back_image = models.ForeignKey(Media,
                                                on_delete=models.CASCADE,
                                                verbose_name=_("Service Page Back Image"),
                                                related_name='service_page_back_image')
    product_page_back_image = models.ForeignKey(Media,
                                                on_delete=models.CASCADE,
                                                verbose_name=_("Product Page Back Image"),
                                                related_name='product_page_back_image')
    contact_page_back_image = models.ForeignKey(Media,
                                                on_delete=models.CASCADE,
                                                verbose_name=_("Contacts Page Back Image"),
                                                related_name='contact_page_back_image')

    def __str__(self):
        return self.main_phone_number

    class Meta:
        verbose_name = _("Common Settings")
        verbose_name_plural = _("Common Settings")


class Feedback(models.Model):
    text = models.TextField(_("text"))

    class Meta:
        verbose_name = _("Feedback")
        verbose_name_plural = _('feedbacks')


