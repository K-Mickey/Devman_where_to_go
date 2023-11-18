from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    fields = [
        "img",
        "image_preview",
        "position",
    ]
    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        return format_html(
            '<img src="{url}" style="max-height: 200px;"/>',
            url=obj.img.url
        )


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image)
