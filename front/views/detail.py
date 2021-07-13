from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from front.models import Recipe
import os.path
from PIL import Image
import json

class DetailView(View):
    template_name = 'detail.html'

    def get(self, request, slug):
        recipe_detail = get_object_or_404(Recipe, slug = slug)
        recipe_detail.ingredients = json.loads(recipe_detail.ingredients)

        return render(request, self.template_name, {"recipe_detail": recipe_detail})