from django.contrib import admin

from common.models import Media, Feedback
# Register your models here.


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'file_type']
    search_fields = ['file_type']
    list_filter = ['file_type']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['text', ]


