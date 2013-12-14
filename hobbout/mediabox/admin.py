from django.contrib import admin

from .models import MediaImage, MediaVideo, MediaFile


class MediaImageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'owner', 'image')
    search_fields = ['pk', 'owner']

admin.site.register(MediaImage, MediaImageAdmin)


class MediaVideoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'owner', 'video_code')
    search_fields = ['pk', 'owner']

admin.site.register(MediaVideo, MediaVideoAdmin)


class MediaFileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'owner', 'doc', 'rank')
    search_fields = ['pk', 'owner']

admin.site.register(MediaFile, MediaFileAdmin)