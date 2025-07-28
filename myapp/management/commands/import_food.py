import csv
from django.core.management.base import BaseCommand
from myapp.models import Food, FoodCategory

class Command(BaseCommand):
    help = 'Імпортує продукти з CSV у базу даних'

    def handle(self, *args, **kwargs):
        with open('data/food_data.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for row in reader:
                category_name = row.get('category')
                category = None
                if category_name:
                    category, _ = FoodCategory.objects.get_or_create(name=category_name)

                Food.objects.create(
                    name=row['name'],
                    category=category,
                    carbs=float(row['carbs']),
                    calories=float(row['calories']),
                    protein=float(row['protein']),
                    fats=float(row['fats']),
                )
                count += 1

        self.stdout.write(self.style.SUCCESS(f'✅ Імпортовано {count} продуктів!'))
