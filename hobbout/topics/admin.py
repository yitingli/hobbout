from django.contrib import admin

from .models import Topic, TopicComment


class TopicAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'content', 'owner')
    search_fields = ['pk', 'name']

admin.site.register(Topic, TopicAdmin)


class TopicCommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'owner', 'topic')
    search_fields = ['pk', 'topic']

admin.site.register(TopicComment, TopicCommentAdmin)
