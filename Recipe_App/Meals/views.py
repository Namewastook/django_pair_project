from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import FoodCombo, Seed_Db

import requests

@login_required(login_url='/')
def meal_select(request):
    return render(request, "Meals/pantry.html")

@login_required(login_url='/')
def seeding_db(request):
    if request.method == "POST":

        a_list = []

        main = ""
        side = ""
        extras = ""
        dishName = ""

        main = request.POST.get("main")
        side = request.POST.get("side")
        extras = request.POST.get("extras")
        dishName = (main + "," + side + "," + extras)

        new_combo = FoodCombo(
            main=main,
            side=side,
            extras=extras,
            dishName=dishName
        )

        a_list.append(new_combo)
        new_combo.save()

    meals = []

    response = eval(
        f'requests.get("https://api.edamam.com/search?q={dishName}&app_id=0890373f&app_key=5c5cb11c82dd77cd32e808aa96589367").json()')

    rec_label = ""
    rec_yield = ""
    rec_calories = ""
    rec_fat_quanity = ""
    rec_carbs_quanity = ""
    rec_protein_quanity = ""

    for i in response['hits']:
        rec_label = (i.get('recipe').get('label'))
        rec_yield = str(int(i.get('recipe').get('yield')))
        rec_calories = str(int(i.get('recipe').get('calories')))
        rec_fat_quanity = str(
            int((i.get('recipe').get("totalNutrients").get("FAT").get("quantity"))))
        rec_carbs_quanity = str(
            int((i.get('recipe').get("totalNutrients").get("CHOCDF").get("quantity"))))
        rec_protein_quanity = str(
            int((i.get('recipe').get("totalNutrients").get("PROCNT").get("quantity"))))

        seeded_db = Seed_Db(
            rec_label=rec_label,
            rec_yield=rec_yield,
            rec_calories=rec_calories,
            rec_fat_quanity=rec_fat_quanity,
            rec_carbs_quanity=rec_carbs_quanity,
            rec_protein_quanity=rec_protein_quanity,
            foodcombo=new_combo
        )

        meals.append(seeded_db)
        seeded_db.save()

    context = {
        "response": meals
    }

    return render(request, "Meals/recipe.html", context)
