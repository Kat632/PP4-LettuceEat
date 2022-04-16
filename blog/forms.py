from django import forms
from .models import Comment, Recipe


class CommentForm(forms.ModelForm):
    """
    Form class to add a comment
    """
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    """
    Form to add a recipe
    """
    class Meta:
        model = Recipe
        fields = [
            'title',
            'slug',
            'excerpt',
            'prep_time',
            'difficulty',
            'serves',
            'cook_time',
            'ingredients',
            'method',
            'featured_image',
        ]

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
