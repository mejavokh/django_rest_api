from django.contrib import admin

from flowers.models import Tags, Flowers, FlowerImage


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['title', ]


@admin.register(Flowers)
class FlowersAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']





