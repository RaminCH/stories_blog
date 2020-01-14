from django.urls import path
from .views import *
from .routers import router

urlpatterns = [
    path('recipes/', RecipeAPIView.as_view(), name='api-recipes' ),
    path('recipes/<int:id>/', RecipeChangeAPI.as_view(), name='api-recipes-change' ),
]

urlpatterns += router.urls 
