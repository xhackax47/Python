from django.db import models


# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=200, default="No Title",
                             blank=True, null=True)
    description = models.CharField(max_length=1000, default="No Description",
                                   blank=True, null=True)
    detail = models.TextField(name="detail", blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="No Name",
                            blank=True, null=True)
    description = models.CharField(max_length=1000, default="No Description",
                                   blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Unit(models.Model):
    name = models.CharField(max_length=200, default="No Name", blank=True, null=True)
    description = models.CharField(max_length=1000, default="No Description", blank=True, null=True)
    is_actual_measure = models.BooleanField(default=True, blank=True, null=True)
    is_visible = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        if self.is_visible:
            return f'{self.name} (Visible)'
        return f'{self.name} (Not visible)'


class RecipeIngredientUnit(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name= 'ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    quantity = models.FloatField(default=1.0, blank=True, null=True)

    class Meta:
        unique_together = ("recipe", "ingredient", "unit")

    def __str__(self):
        return f"{self.recipe} - {self.quantity} {self.unit} {self.ingredient}"
