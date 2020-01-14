from rest_framework.routers import DefaultRouter
from .views import RecipeAPIViewSet

router = DefaultRouter()

router.register(r'recipes-api', RecipeAPIViewSet)
# router.register(r'stories-api', RecipeAPIViewSet)