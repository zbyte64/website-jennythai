from django.contrib import admin
from models import Gallery, Photo

class PhotoAdminInline(admin.StackedInline):
    model = Photo

class GalleryAdmin(admin.ModelAdmin):
    #class Media:
        #js = ['http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js',
         #     'http://jquery.malsup.com/form/jquery.form.js',
         #     '/media/js/upload.js']

    list_display = ['name', 'active', 'order']
    list_filter = ['active']
    list_editable = ['active', 'order']
    prepopulated_fields = {'slug':('name',)}
    inlines = [PhotoAdminInline]

admin.site.register(Gallery, GalleryAdmin)
