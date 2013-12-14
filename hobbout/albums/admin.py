from django.contrib import admin

from .models import Album


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'cover', 'description')
    search_fields = ['pk', 'name']

admin.site.register(Album, AlbumAdmin)

"""
class FrameCommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'owner', 'content', 'parent_comment')
    search_fields = ['pk', 'owner']

admin.site.register(FrameComment, FrameCommentAdmin)
"""
