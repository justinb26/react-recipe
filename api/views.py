from rest_framework import generics
  
from .models import Book, Recipe, Ingredient, ScheduleEntry
from .serializers import BookSerializer, RecipeSerializer, IngredientSerializer, ScheduleEntrySerializer


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
