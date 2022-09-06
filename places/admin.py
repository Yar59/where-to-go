from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableTabularInline, SortableAdminBase

from .models import Place, Image


class ImageInline(SortableTabularInline):
    model = Image
    fields = (
        ('image', 'preview'),
        'ordinal_number'
    )
    readonly_fields = ["preview", ]
    extra = 0

    def preview(self, obj):
        return format_html(f'<img src="{obj.image.url}" style="max-height: 200px;">')


@admin.register(Place)
class PlasceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline, ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = (
        'image',
        'preview',
        'place',
        'ordinal_number',
    )
    raw_id_fields = ['place',]
    readonly_fields = ["preview",]

    def preview(self, obj):
        return format_html(f'<img src="{obj.image.url}" style="max-height: 200px;">')

