from django.urls import path
from . import views


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('add-recipe/', views.create_recipe, name='create_recipe'),
    path('edit-recipe/<slug:slug>', views.edit_recipe, name='edit_recipe'),
    path('delete-recipe/<slug:slug>', views.delete_recipe,
         name='delete_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>/', views.RecipeLike.as_view(), name='recipe_like'),
]
