from django.contrib import admin

from app.models import Recipe, Ingredient, Unit, RecipeIngredientUnit

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(RecipeIngredientUnit)
