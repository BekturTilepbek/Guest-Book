from django.contrib import admin

from webapp.models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'created_at', 'updated_at', 'status']
    list_display_links = ['id', 'name']
    list_filter = ['status']
    search_fields = ['name']
    fields = ['name', 'email', 'text', 'status']


admin.site.register(Entry, EntryAdmin)
