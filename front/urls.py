from django.urls import path

from .views.auth import login, signup
from .views import index, add_recipe, detail, search, custome, my_recipe

urlpatterns = [
    path('login/', login.LoginView.as_view(), name='user_login'),
    path('logout/', login.logout, name='user_logout'),
    path('signup/', signup.SignUpView.as_view(), name='user_signup'),
    path('', index.IndexView.as_view(), name='home'),
    path('add-recipe/', add_recipe.AddRecipeView.as_view(), name='add_recipe'),
    path('detail/<slug:slug>/', detail.DetailView.as_view(), name='detail'),
    path('search/', search.SearchView.as_view(), name='search'),
    path('edit/<slug:slug>/', custome.EditView.as_view(), name='edit'),
    path('edit-recipe/', custome.EditView.as_view(), name='edit'),
    path('delete-recipe/', custome.DeleteView.as_view(), name='delete'),
    path('Breakfast/', search.SearchView.as_view(), name='breakfast'),
    path('Lunch/', search.SearchView.as_view(), name='lunch'),
    path('Dinner/', search.SearchView.as_view(), name='dinner'),
    path('Beverages/', search.SearchView.as_view(), name='beverage'),
    path('my-recipes/', my_recipe.MyRecipeView.as_view(), name='my_recipe'),
]
