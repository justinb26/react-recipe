from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response

from .models import Book, Recipe, Ingredient, ScheduleEntry, Tag
from .serializers import BookSerializer, RecipeSerializer, IngredientSerializer, ScheduleEntrySerializer, TagSerializer


class BookList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating Book objects
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class IngredientList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating Book objects
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    
          
class RecipeList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating Book objects
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
          

class ScheduleEntryList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating Book objects
    """
    queryset = ScheduleEntry.objects.all()
    serializer_class = ScheduleEntrySerializer

class TagList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating tags
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(data=serializer.data)