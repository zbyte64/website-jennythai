from django.contrib import admin
from forms import GalleryForm
from models import Gallery

class GalleryAdmin(admin.ModelAdmin):
    form = GalleryForm
    
    list_display = ['name', 'active', 'order']
    list_filter = ['active']
    list_editable = ['active', 'order']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Gallery, GalleryAdmin)

