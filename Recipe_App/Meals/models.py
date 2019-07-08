from django.db import models

# Create your models here.
from django.db import models


class FoodCombo(models.Model):
    main = models.CharField(max_length=50)
    side = models.CharField(max_length=50)
    extras = models.CharField(max_length=50)
    dishName = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.main}, {self.side}, {self.extras}, By your powers combined, I am -> {self.dishName}"


class Seed_Db(models.Model):
    rec_label = models.CharField(max_length=50)
    rec_yield = models.CharField(max_length=50)
    rec_calories = models.CharField(max_length=50)
    rec_fat_quanity = models.CharField(max_length=50)
    rec_carbs_quanity = models.CharField(max_length=50)
    rec_protein_quanity = models.CharField(max_length=50)
    foodcombo = models.ForeignKey(FoodCombo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Recipe name: {self.rec_label}, Servings: {self.rec_yield}, Calories: {self.rec_calories}, Grams of Fat: {self.rec_fat_quanity}, Grams of Carbs: {self.rec_carbs_quanity}, Grams of Protein: {self.rec_protein_quanity}"
