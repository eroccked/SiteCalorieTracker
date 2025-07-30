# import csv
# from django.core.management.base import BaseCommand
# from myapp.models import Food, FoodCategory
#
# class Command(BaseCommand):
#     help = 'Імпортує продукти з CSV у базу даних'
#
#     def handle(self, *args, **kwargs):
#         with open('data/food_data.csv', newline='', encoding='utf-8') as csvfile:
#             reader = csv.DictReader(csvfile)
#             count = 0
#             for row in reader:
#                 category_name = row.get('category')
#                 category = None
#                 if category_name:
#                     category, _ = FoodCategory.objects.get_or_create(name=category_name)
#
#                 Food.objects.create(
#                     name=row['name'],
#                     category=category,
#                     carbs=float(row['carbs']),
#                     calories=float(row['calories']),
#                     protein=float(row['protein']),
#                     fats=float(row['fats']),
#                 )
#                 count += 1
#
#         self.stdout.write(self.style.SUCCESS(f'✅ Імпортовано {count} продуктів!'))

from django.core.management.base import BaseCommand, CommandError
from myapp.models import Food, FoodCategory  # Імпортуємо обидві моделі

# Імпортуємо дані з food_data.py
# Переконайтеся, що food_data.py знаходиться в папці myapp
try:
    from myapp.food_data import FOOD_DATA
except ImportError:
    raise CommandError("Файл food_data.py не знайдено в myapp/. Будь ласка, створіть його.")


class Command(BaseCommand):
    help = 'Імпортує дані про продукти та їх категорії з попередньо визначеного списку.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Починаю імпорт продуктів...'))

        # Зберігаємо унікальні категорії
        unique_categories = set(item['category'] for item in FOOD_DATA)
        for category_name in unique_categories:
            category, created = FoodCategory.objects.get_or_create(name=category_name)
            if created:
                self.stdout.write(f'Створено категорію: {category.name}')
            else:
                self.stdout.write(f'Категорія вже існує: {category.name}')

        # Імпортуємо продукти
        imported_count = 0
        for item in FOOD_DATA:
            category_name = item['category']
            category = FoodCategory.objects.get(name=category_name)  # Отримуємо об'єкт категорії

            # Створюємо або отримуємо продукт.
            # Якщо продукт з такою назвою та поживними значеннями вже існує, ми його не створюємо заново.
            # Це допомагає уникнути дублікатів при повторному запуску команди.
            food, created = Food.objects.get_or_create(
                name=item['name'],
                carbs=item['carbs'],
                calories=item['calories'],
                protein=item['protein'],
                fats=item['fats'],
                defaults={'category': category}  # Встановлюємо категорію лише при створенні
            )
            if created:
                imported_count += 1
                self.stdout.write(f'Імпортовано продукт: {food.name} ({food.category.name})')
            else:
                self.stdout.write(f'Продукт вже існує: {food.name}')

        self.stdout.write(self.style.SUCCESS(f'Успішно імпортовано {imported_count} нових продуктів.'))
        self.stdout.write(self.style.SUCCESS('Імпорт завершено.'))
