from django.urls import path
from . import views


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('add-recipe/', views.create_recipe, name='create_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>/', views.RecipeLike.as_view(), name='recipe_like'),
]
