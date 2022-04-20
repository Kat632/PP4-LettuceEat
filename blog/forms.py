from django import forms
from .models import Comment, Recipe
from django_summernote.widgets import SummernoteInplaceWidget


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
            'excerpt',
            'prep_time',
            'difficulty',
            'serves',
            'cook_time',
            'ingredients',
            'method',
            'featured_image',
        ]

        widgets = {
            'ingredients': SummernoteInplaceWidget(),
            'method': SummernoteInplaceWidget()
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
