from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
LEVEL = ((0, "Easy"), (1, "Regular"), (2, "Hard"))

class Recipe(models.Model):
    """
    Model for the Recipe
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes")
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    prep_time = models.IntegerField(default=0)
    difficulty = models.IntegerField(choices=LEVEL, default=0)
    serves = models.IntegerField(default=1)
    cook_time = models.IntegerField(default=0)
    ingredients = models.TextField(default="",
                                blank=False, null=False)
    method = models.TextField(blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(
        User,
        related_name='recipe_likes',
        blank=True
    )

    class Meta:
        """
        Order the recipes in descending order.
        """
        ordering = ['-created_on']
    
    def __str__(self):
        """
        Returns a string showing the title.
        """
        return str(self.title)
    
    def amount_of_likes(self):
        """
        See number of likes on a recipe.
        """
        return self.likes.count()

    def can_edit(self, request, slug):
        """
        Allows author to edit recipe.
        """
        if self.author:
            return True
        else:
            return False

    def can_delete(self, request, slug):
        """
        Allows author to delete recipe.
        """
        if self.author:
            return True
        else:
            return False


class Comment(models.Model):
    """
    Add a comment.
    """
    post = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Order by oldest comment first
        """
        ordering = ['created_on']
    
    def __str__(self):
        return f"Comment {self.body} by {self.name}"