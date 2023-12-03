from django.contrib import admin

from education.models import Subject, Branch, Material

admin.site.register(Subject)

admin.site.register(Branch)


@admin.register(Material)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'date_of_last_modification', 'branch', 'owner',)
    list_filter = ('branch', 'owner',)
    search_fields = ('title', 'owner')
