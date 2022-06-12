from django.db import models
# Create your models here.

""" class Recipe(models.Model):
    DIFFICULTY_LEVELS = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    )
    name = models.CharField(max_length=120)
    ingredients = models.CharField(max_length=400)
    picture = models.FileField()
    difficulty = models.CharField(choices=DIFFICULTY_LEVELS, max_length=10)
    prep_time = models.PositiveIntegerField()
    prep_guide = models.TextField()

    def __str_(self):
        return "Recipe for {}".format(self.name) """


class Deinosti(models.Model):
    title = models.CharField(max_length=90)
    description = models.TextField()

class Step(models.Model):
    image = models.FileField()
    title = models.CharField(max_length=50)
    description = models.TextField()