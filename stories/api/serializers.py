from rest_framework import serializers
from stories.models import Recipe, Category
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'full_name',
        ]
    def get_full_name(self, obj):
        return "{} {}".format(obj.first_name, obj.last_name)



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'image'
        ]


class RecipeSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    owner = UserSerializer()
    class Meta:
        model = Recipe
        fields = [
            'id',
            'title',
            'image',
            'description',
            # 'long_description',
            'category',
            'owner',
            'view_count',
        ]

class RecipeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'image',
            'description',
            # 'long_description',
            'category',
            'owner',
        ]