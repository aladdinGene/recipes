from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from front.models import Recipe
from django.http import JsonResponse
from django.http import QueryDict
from PIL import Image
import os.path

class EditView(View):
    template_name = 'add-new.html'

    def get(self, request, slug):
        recipe_detail = get_object_or_404(Recipe, slug = slug)
        cook_times = ["no cooking required", "Less than 10 mins", "10-30 mins", "Less than 30 mins", "30 mins to 1 hour", "1-2 hours", "2-3 hours", "More than 3 hours"]
        categories = ["Breakfast", "Lunch", "Dinner", "Beverages"]

        if request.user.is_authenticated:
            return render(request, self.template_name, {"recipe_detail": recipe_detail, "cook_times": cook_times, "categories": categories})
        else:
            return redirect('/login/')

    def post(self, request):
        if request.user.is_authenticated:
            try:
                current_user = request.user
                post_value = request.POST
                recipe = Recipe.objects.filter(slug=post_value['slug'])[0]
                if request.FILES and request.FILES['image']:
                    if request.FILES['image'].content_type == 'image/jpeg' or request.FILES['image'].content_type == 'image/png' or request.FILES['image'].content_type == 'image/jpg':
                        try:
                            im = Image.open(request.FILES['image'].file)
                            im.verify()
                        except:
                            return JsonResponse({'status': 400, 'message': 'Invalid image'})
                            
                    request.FILES['image'].name = str(current_user.id) + os.path.splitext(request.FILES['image'].name)[1].lower()
                    recipe.title = post_value['title']
                    recipe.category = post_value['category']
                    recipe.description = post_value['description']
                    recipe.ingredients = post_value['ingredients']
                    recipe.method = post_value['method']
                    recipe.prepare_time = post_value['prepare_time']
                    recipe.cook_time = post_value['cook_time']
                    recipe.image = request.FILES['image']
                    recipe.save()
                else:
                    recipe.title = post_value['title']
                    recipe.category = post_value['category']
                    recipe.description = post_value['description']
                    recipe.ingredients = post_value['ingredients']
                    recipe.method = post_value['method']
                    recipe.prepare_time = post_value['prepare_time']
                    recipe.cook_time = post_value['cook_time']
                    if post_value['edit_image_num'] == '0':
                        recipe.image = 'images/default.png'
                    recipe.save()

            except Exception as e:
                return JsonResponse({'status': 400, 'message': str(e)})

            return JsonResponse({'status': 200, 'message': recipe.slug })
        else:
            return JsonResponse({'status': 400, 'message': 'You must login.'})

class DeleteView(View):
    def post(self, request):
        try:
            post_value = request.POST
            slug = post_value['slug']
            recipe = Recipe.objects.filter(slug=slug)
            recipe.delete()
        except Exception as e:
            return JsonResponse({'status': 400, 'message': str(e)})

        return JsonResponse({'status': 200, 'message': slug })
