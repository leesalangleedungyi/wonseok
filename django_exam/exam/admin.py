from tkinter.colorchooser import Chooser
from django.contrib import admin
from .models import Choice,Question

admin.site.register(Question) 
admin.site.register(Choice) 