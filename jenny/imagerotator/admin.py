from django.contrib import admin
from models import *

class RotatorImageInline(admin.TabularInline):
    model = RotatorImage

class RotatorAdmin(admin.ModelAdmin):
    inlines = [RotatorImageInline]

admin.site.register(Rotator, RotatorAdmin)

