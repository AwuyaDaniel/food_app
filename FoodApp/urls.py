from django.urls import path
from django.conf.urls.static import static

from Food import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes', views.recipe, name='recipe'),
    path('single_recipe/<int:id>/', views.single_recipe, name='single_recipe'),


    path('restaurants', views.restaurants, name='restaurants'),
    path('single_restaurant/<int:id>/', views.single_restaurants, name='single_restaurants'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = 'food'
