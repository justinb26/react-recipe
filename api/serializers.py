from rest_framework import serializers

from .models import Book, Recipe, Ingredient, ScheduleEntry


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'author')


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('title', 'quantity', 'recipe')


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
     )
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'ingredients')


class ScheduleEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = ScheduleEntry
        fields = ('entryDate', 'breakfastEntry', 'lunchEntry', 'dinnerEntry')
