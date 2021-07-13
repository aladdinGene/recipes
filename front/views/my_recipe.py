from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from front.models import Recipe


class MyRecipeView(View):
    template_name = 'index.html'

    # @login_required(login_url="/login/")
    def get(self, request):
        current_user = request.user
        recipes = Recipe.objects.filter(uploader=current_user.id)
        category = 'My Recipes'

        return render(request, self.template_name, {'recipes': recipes, 'category': category})