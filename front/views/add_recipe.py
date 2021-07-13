from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from front.models import Recipe
import os.path
from PIL import Image


class AddRecipeView(View):
    template_name = 'add-new.html'

    def get(self, request):
        cook_times = ["Less than 30 mins", "30 mins to 1 hour", "1-2 hours", "2-3 hours", "More than 3 hours"]
        categories = ["Breakfast", "Lunch", "Dinner", "Beverages"]

        if request.user.is_authenticated:
            return render(request, self.template_name, {"cook_times": cook_times, "categories": categories})
        else:
            return redirect('/login/')

    def post(self, request):
        try:
            current_user = request.user
            post_value = request.POST
            
            if request.FILES and request.FILES['image']:
                if request.FILES['image'].content_type == 'image/jpeg' or request.FILES['image'].content_type == 'image/png' or request.FILES['image'].content_type == 'image/jpg':
                    try:
                        im = Image.open(request.FILES['image'].file)
                        im.verify()
                    except:
                        return JsonResponse({'status': 400, 'message': 'Invalid image'})
                        
                request.FILES['image'].name = str(current_user.id) + os.path.splitext(request.FILES['image'].name)[1].lower()
                recipe = Recipe.objects.create(title=post_value['title'], category=post_value['category'], description=post_value['description'],
                                    ingredients=post_value['ingredients'], method=post_value['method'], prepare_time=post_value['prepare_time'],
                                    cook_time=post_value['cook_time'], uploader=current_user.id)
                recipe.image = request.FILES['image']
                recipe.save()
            else:
                recipe = Recipe.objects.create(title=post_value['title'], category=post_value['category'], description=post_value['description'],
                                    ingredients=post_value['ingredients'], method=post_value['method'], prepare_time=post_value['prepare_time'],
                                    cook_time=post_value['cook_time'], uploader=current_user.id)
                recipe.save()

        except Exception as e:
            return JsonResponse({'status': 400, 'message': str(e)})

        return JsonResponse({'status': 200, 'message': recipe.slug })