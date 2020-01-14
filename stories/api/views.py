from rest_framework.views import APIView
from stories.models import Recipe
from django.http import JsonResponse
from .serializers import RecipeSerializer, RecipeCreateSerializer
from rest_framework.viewsets import ModelViewSet

class RecipeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True, context={
            'request': request
        })
        return JsonResponse({
            'recipes': serializer.data
        })

    def post(self, request, *args, **kwargs):
        recipe_data = request.data
        serializer = RecipeCreateSerializer(data=recipe_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors)


class RecipeChangeAPI(APIView):
    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.get(id=kwargs.get('id'))
        serializer = RecipeSerializer(recipes, context={
            'request': request
        })
        return JsonResponse({
            'recipes': serializer.data
        })

    def put(self, request, *args, **kwargs):
        recipe = Recipe.objects.get(id=kwargs.get('id'))
        updated_recipe_data = request.data
        serializer = RecipeCreateSerializer(data=updated_recipe_data, instance=recipe)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    def patch(self, request, *args, **kwargs):
        recipe = Recipe.objects.get(id=kwargs.get('id'))
        updated_recipe_data = request.data
        serializer = RecipeCreateSerializer(data=updated_recipe_data, instance=recipe, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    def delete(self, request, *args, **kwargs):
        recipe = Recipe.objects.get(id=kwargs.get('id')).first()
        if recipe:
            recipe.delete()
            return JsonResponse({}, status=204)
        return JsonResponse({
                'detail': 'Not found',
            }, status=404)


class RecipeAPIViewSet(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateSerializer