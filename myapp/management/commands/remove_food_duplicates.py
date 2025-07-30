from django.core.management.base import BaseCommand, CommandError
from django.db.models import Count
from myapp.models import Food # Імпортуємо модель Food
from django.db.models.functions import Lower # Додано для перетворення в нижній регістр
from django.db.models import F # Додано для посилань на поля

class Command(BaseCommand):
    help = 'Видаляє дублікати записів у моделі Food, залишаючи лише один, на основі нормалізованої назви та поживних значень.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Пошук та видалення дублікатів їжі...'))

        # Знаходимо дублікати за комбінацією нормалізованої назви, вуглеводів, калорій, білків та жирів
        # Використовуємо Lower для порівняння без урахування регістру
        duplicate_foods_query = Food.objects.annotate(
            normalized_name=Lower('name') # Створюємо анотовану колонку з назвою в нижньому регістрі
        ).values('normalized_name', 'carbs', 'calories', 'protein', 'fats').annotate(
            item_count=Count('id')
        ).filter(item_count__gt=1)

        total_deleted = 0

        if not duplicate_foods_query.exists():
            self.stdout.write(self.style.WARNING('Дублікатів їжі не знайдено за вказаними критеріями.'))
            return

        for item_data in duplicate_foods_query:
            # Отримуємо значення для фільтрації, використовуючи нормалізовану назву
            food_normalized_name = item_data['normalized_name']
            food_carbs = item_data['carbs']
            food_calories = item_data['calories']
            food_protein = item_data['protein']
            food_fats = item_data['fats']

            self.stdout.write(f'Знайдено дублікати для: "{food_normalized_name}" (К:{food_carbs}, Кал:{food_calories}, Б:{food_protein}, Ж:{food_fats})')

            # Отримуємо всі записи, що відповідають цим критеріям,
            # сортуємо за ID (щоб залишити найменший ID)
            # і пропускаємо перший (який ми хочемо зберегти).
            # Фільтруємо за оригінальною назвою, але порівнюємо її в нижньому регістрі
            foods_to_delete = Food.objects.filter(
                name__iexact=food_normalized_name, # Використовуємо __iexact для порівняння без урахування регістру
                carbs=food_carbs,
                calories=food_calories,
                protein=food_protein,
                fats=food_fats
            ).order_by('id')[1:]

            if foods_to_delete.exists():
                num_deleted_for_item = foods_to_delete.count()
                for food in foods_to_delete:
                    food.delete() # Видаляємо кожен дублікат
                total_deleted += num_deleted_for_item
                self.stdout.write(self.style.WARNING(f'  Видалено {num_deleted_for_item} дублікатів.'))
            else:
                self.stdout.write(f'  Дублікатів для "{food_normalized_name}" не знайдено (можливо, вже видалено).')

        if total_deleted > 0:
            self.stdout.write(self.style.SUCCESS(f'Успішно видалено {total_deleted} дублікатів їжі.'))
        else:
            self.stdout.write(self.style.WARNING('Дублікатів їжі не знайдено після повторної перевірки.'))

