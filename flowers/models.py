from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import Media, Feedback


class Tags(models.Model):
    title = models.CharField(max_length=120)

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __str__(self):
        return self.title


class Flowers(models.Model):
    title = models.CharField(_('title'), max_length=120)
    occasion = models.CharField(_('occasion'), max_length=120)
    to_whom = models.CharField(_('to_whom'), max_length=120)
    price = models.IntegerField(_('price'))
    desc = models.TextField(_('desc'),)
    feedback = models.ForeignKey(Feedback, verbose_name=_('feedback'),
                                 on_delete=models.CASCADE)
    tags = models.ForeignKey(Tags, verbose_name=_('tags'),
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Flower")
        verbose_name_plural = _("Flowers")

    def __str__(self):
        return self.title


class FlowerImage(models.Model):
    image = models.ForeignKey(Media, on_delete=models.CASCADE,
                              verbose_name=_('image'))
    flower = models.ForeignKey(Flowers, on_delete=models.CASCADE,
                               verbose_name=_('flower'),
                               related_name=_('flower_image'))

    class Meta:
        verbose_name = _('flower_image')
        verbose_name_plural = _('flower_images')

    def __str__(self):
        return f"Image Id: {self.id}| Flower: {self.product.title}"
