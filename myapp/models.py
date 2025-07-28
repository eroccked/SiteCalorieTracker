from django.db import models
from django.contrib.auth.models import User


class FoodCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(FoodCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='foods')
    carbs = models.FloatField()
    calories = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()

    def __str__(self):
        return self.name

class Consume(models.Model):
    MEAL_TYPES = [
        ('breakfast', 'Сніданок'),
        ('lunch', 'Обід'),
        ('dinner', 'Вечеря'),
        ('snack', 'Перекус'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=10, choices=MEAL_TYPES)
    date = models.DateField()
    weight = models.FloatField(default=100)  # вага порції, за замовчуванням 100 грамів

    def __str__(self):
        return f"{self.user} - {self.food} ({self.meal_type}) - {self.weight}g"
