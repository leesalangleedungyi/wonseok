from django.contrib import admin
from .models import Content,Image

class ImageInline(admin.TabularInline):
    model = Image

class ContentAdmin(admin.ModelAdmin):
    list_display=("user","text")
    inlines=[ImageInline]
    
admin.site.register(Content,ContentAdmin)