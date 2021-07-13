from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from front.models import Recipe


class SearchView(View):
    template_name = 'index.html'

    # @login_required(login_url="/login/")
    def get(self, request):
        title = request.GET.get('title','')
        if title == '':
            category = request.path.split('/')[-2]
            recipes = Recipe.objects.filter(category=category)
        else:
            category = request.GET['category']
            if category == 'All':
                recipes = Recipe.objects.filter(title__icontains=title)
            else:
                recipes = Recipe.objects.filter(title__icontains=title, category=category)
        return render(request, self.template_name, {'recipes': recipes, 'category': category})