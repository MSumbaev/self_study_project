from django.contrib import admin

from education.models import Subject, Branch, Material


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'subject',)
    list_filter = ('subject',)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'date_of_last_modification', 'branch', 'owner',)
    list_filter = ('branch', 'owner',)
    search_fields = ('title', 'owner')
