from dataclasses import fields
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude_fields = ['register_dttm']