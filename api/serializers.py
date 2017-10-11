from rest_framework import serializers

from .models import Book, Recipe, Ingredient, ScheduleEntry, Tag


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'author')


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('id', 'title', 'quantity', 'recipe')


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
     )
    # tags = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='phrase'
    # )
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'description', 'ingredients', 'tags')


class ScheduleEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = ScheduleEntry
        fields = ('id', 'entryDate', 'breakfastEntry', 'lunchEntry', 'dinnerEntry')


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'phrase', 'recipe')

    def create(self, validated_data):
        tag, created = Tag.objects.update_or_create(

            phrase=validated_data.get('phrase', None),
            recipe = validated_data.get('recipe', None),
        )

        return tag