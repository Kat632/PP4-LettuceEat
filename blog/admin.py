from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Use Summernote for recipe admin
    """
    summernote_fields = ('content')
