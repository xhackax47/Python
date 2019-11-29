from django.views import generic

from app.models import Recipe


class IndexView(generic.TemplateView):
    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['name'] = "Samy"
        result['recipes'] = Recipe.objects.all()
        return result

    template_name = "index.html"


class RecipeListView(generic.ListView):
    model = Recipe
    template_name = "recipes_list.html"


class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = "recipes_detail.html"
