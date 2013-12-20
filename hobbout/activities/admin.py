from django.contrib import admin

from .models import Activity, ActivityComment, UserActivityBridge


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'content', 'owner')
    search_fields = ['pk', 'name']

admin.site.register(Activity, ActivityAdmin)


class ActivityCommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'owner', 'activity')
    search_fields = ['pk', 'activity']

admin.site.register(ActivityComment, ActivityCommentAdmin)


class UserActivityBridgeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'activity')
    search_fields = ['pk', 'user', 'activity']

admin.site.register(UserActivityBridge, UserActivityBridgeAdmin)
