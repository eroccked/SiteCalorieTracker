from django.db import models
from django.contrib.auth.models import User  # Імпортуємо стандартну модель User
from datetime import date  # <--- Додано імпорт date з datetime


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

    @property
    def carbs_weighted(self):
        if self.food:
            return self.food.carbs * (self.weight / 100)
        return 0.0

    @property
    def calories_weighted(self):
        if self.food:
            return self.food.calories * (self.weight / 100)
        return 0.0

    @property
    def protein_weighted(self):
        if self.food:
            return self.food.protein * (self.weight / 100)
        return 0.0

    @property
    def fats_weighted(self):
        if self.food:
            return self.food.fats * (self.weight / 100)
        return 0.0


# Модель UserProfile
class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Чоловік'),
        ('female', 'Жінка'),
        ('other', 'Інше'),
    ]

    ACTIVITY_LEVEL_CHOICES = [
        ('sedentary', 'Сидячий (мало або без фізичної активності)'),
        ('light', 'Легка активність (1-3 дні на тиждень)'),
        ('moderate', 'Помірна активність (3-5 днів на тиждень)'),
        ('active', 'Висока активність (6-7 днів на тиждень)'),
        ('very_active', 'Дуже висока активність (щоденні інтенсивні тренування)'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    height = models.FloatField(verbose_name="Зріст (см)", null=True, blank=True)
    weight = models.FloatField(verbose_name="Вага (кг)", null=True, blank=True)

    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        null=True,
        blank=True,
        default='profile_pics/profile.png',
        verbose_name="Фото профілю"
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        null=True,
        blank=True,
        verbose_name="Стать"
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата народження"
    )
    activity_level = models.CharField(
        max_length=20,
        choices=ACTIVITY_LEVEL_CHOICES,
        default='sedentary',
        verbose_name="Рівень активності"
    )
    allergies = models.TextField(
        blank=True,
        verbose_name="Алергії (перелічіть через кому)",
        help_text="Наприклад: горіхи, лактоза, глютен"
    )
    desired_weight = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Бажана вага (кг)"
    )

    def __str__(self):
        return f"Профіль {self.user.username}"

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - (
                        (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return None

    @property
    def bmi(self):
        if self.height and self.weight and self.height > 0:
            height_in_meters = self.height / 100
            return self.weight / (height_in_meters ** 2)
        return None
