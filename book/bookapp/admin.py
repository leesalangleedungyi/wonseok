from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('code','title')

admin.site.register(Book,BookAdmin)