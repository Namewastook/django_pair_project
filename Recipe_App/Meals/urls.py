from django.urls import path
from . import views

urlpatterns = [
    path('', views.meal_select, name='Pantry'),
    path('recipes/', views.seeding_db, name='Recipe'),

]
