from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('recipes/', views.recipes, name="recipes"),
    path('delete_recipe/<id>/', views.delete_recipe, name="delete_recipe"),
    path('update/<id>/', views.update, name="update"),
    path('login/', views.login_page, name="login_page"),
    path('register/', views.register_page, name="register_page"),
    path('logout/', views.logout_page, name="logout_page")
]