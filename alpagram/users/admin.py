from django.contrib import admin

from .models import CustomUser,Profile

class CustomAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "nickname")

admin.site.register(CustomUser,CustomAdmin)
admin.site.register(Profile)