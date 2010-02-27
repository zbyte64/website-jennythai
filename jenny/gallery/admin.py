from django.contrib import admin
from forms import GalleryForm
from models import Gallery, Photo

class PhotoAdminInline(admin.StackedInline):
    model = Photo

class GalleryAdmin(admin.ModelAdmin):
    form = GalleryForm
    
    class Media:
        js = ['http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js',]
    
    list_display = ['name', 'active', 'order']
    list_filter = ['active']
    list_editable = ['active', 'order']
    prepopulated_fields = {'slug':('name',)}
    inlines = [PhotoAdminInline]

admin.site.register(Gallery, GalleryAdmin)

