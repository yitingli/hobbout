from django.contrib import admin

from .models import Group, UserGroupBridge


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'owner', 'area', 'location')
    search_fields = ['pk', 'name']

admin.site.register(Group, GroupAdmin)


class UserGroupBridgeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'group', 'role', 'post_num')
    search_fields = ['pk', 'user']

admin.site.register(UserGroupBridge, UserGroupBridgeAdmin)
