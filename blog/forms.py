from  .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form class to add a comment
    """
    class Meta:
        model = Comment
        fields = ('body',)