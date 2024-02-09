from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)
router.register('recipes', views.RecipeViewSet)
"""
for upload image -> http://127.0.0.1:8000/api/recipe/recipes/{id}/upload-image/
for filter -> http://127.0.0.1:8000/api/recipe/recipes/?tags=2&ingredients=1
              http://127.0.0.1:8000/api/recipe/recipes/?tags=2
              http://127.0.0.1:8000/api/recipe/recipes/?ingredients=1
for filtering tags assigned to recipes -> http://127.0.0.1:8000/api/recipe/tags/?assigned_only=1
for filtering ingredients assigned to recipes -> http://127.0.0.1:8000/api/recipe/ingredients/?assigned_only=1
"""

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
