from django.contrib import admin

from .models import Area, Location


class AreaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description')
    search_fields = ['pk', 'name']

admin.site.register(Area, AreaAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'area', 'description')
    search_fields = ['pk', 'name']

admin.site.register(Location, LocationAdmin)
