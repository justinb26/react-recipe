from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=100)



class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)


class Ingredient(models.Model):
    title = models.CharField(max_length=200, unique=True)
    quantity = models.CharField(max_length=200)
    recipe = models.ForeignKey(Recipe)

class ScheduleEntry(models.Model):
    entryDate = models.DateField()
    breakfastEntry = models.ForeignKey(Recipe, related_name="breakfast")
    lunchEntry = models.ForeignKey(Recipe, related_name="lunch")
    dinnerEntry = models.ForeignKey(Recipe, related_name="dinner")