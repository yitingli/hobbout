from django.contrib import admin

from .models import MediaFrame, FrameComment


class MediaFrameAdmin(admin.ModelAdmin):
    list_display = ('pk', 'owner', 'album', 'description', 'content_type')
    search_fields = ['pk', 'owner']

admin.site.register(MediaFrame, MediaFrameAdmin)


class FrameCommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'owner', 'content', 'parent_comment')
    search_fields = ['pk', 'owner']

admin.site.register(FrameComment, FrameCommentAdmin)
