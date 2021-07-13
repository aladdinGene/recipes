from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from front.models import Recipe


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        recipes = Recipe.objects.all()
        return render(request, self.template_name, {'recipes': recipes})