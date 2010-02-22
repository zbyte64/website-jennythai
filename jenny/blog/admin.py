from django.contrib import admin
from adminfiles.admin import FilePickerAdmin

from models import BlogEntry

class BlogEntryAdmin(FilePickerAdmin):
    list_display = ['title', 'active', 'date']
    list_filter = ['active', 'date']
    list_editable = ['active']
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'date'
    adminfiles_fields = ['body']

admin.site.register(BlogEntry, BlogEntryAdmin)
