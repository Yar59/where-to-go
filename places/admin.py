from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlasceAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = (
        'image',
        'preview',
        'place',
    )
    raw_id_fields = ['place',]
    readonly_fields = ["preview",]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')

