from django.core.management.base import BaseCommand, CommandError
from myapp.models import Food, FoodCategory
import pandas as pd
import os
from django.conf import settings


class Command(BaseCommand):
    help = 'Імпортує дані про продукти та їх категорії з великого CSV-файлу Open Food Facts.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='data/en.openfoodfacts.org.products.csv',  # Шлях за замовчуванням у папці data
            help='Шлях до CSV-файлу Open Food Facts (наприклад, data/en.openfoodfacts.org.products.csv)'
        )
        parser.add_argument(
            '--limit',
            type=int,
            default=None,  # Без ліміту за замовчуванням
            help='Обмежити кількість імпортованих продуктів (для тестування).'
        )

    def handle(self, *args, **options):
        file_path = options['file']
        limit = options['limit']

        full_file_path = os.path.join(settings.BASE_DIR, file_path)

        if not os.path.exists(full_file_path):
            raise CommandError(f"Файл не знайдено за шляхом: {full_file_path}")

        self.stdout.write(self.style.SUCCESS(f'Починаю імпорт продуктів з {full_file_path}...'))

        try:
            # Читаємо тільки заголовок, щоб отримати доступні колонки
            temp_df = pd.read_csv(full_file_path, sep='\t', nrows=0)
            available_cols = temp_df.columns.tolist()

            # Визначаємо обов'язкові та опціональні колонки
            required_cols = [
                'product_name', 'categories_en', 'carbohydrates_100g',
                'energy-kcal_100g', 'proteins_100g', 'fat_100g'
            ]
            optional_cols = ['product_name_uk']

            # Формуємо фінальний список колонок для завантаження
            final_usecols = []
            for col in required_cols:
                if col not in available_cols:
                    raise CommandError(f"Обов'язкова колонка '{col}' не знайдена у CSV-файлі. Перевірте файл.")
                final_usecols.append(col)

            for col in optional_cols:
                if col in available_cols:
                    final_usecols.append(col)
                else:
                    self.stdout.write(
                        self.style.WARNING(f"Опціональна колонка '{col}' не знайдена у CSV-файлі. Продовжую без неї."))

            # Читаємо CSV-файл за допомогою pandas
            # Змінено: читаємо числові колонки як 'object' спочатку
            df = pd.read_csv(
                full_file_path,
                sep='\t',
                usecols=final_usecols,
                dtype={
                    'product_name': str,
                    'categories_en': str,
                    # Змінено: читаємо як 'object' для стійкості до помилок
                    'carbohydrates_100g': object,
                    'energy-kcal_100g': object,
                    'proteins_100g': object,
                    'fat_100g': object
                },
                low_memory=False
            )
            self.stdout.write('Файл CSV успішно завантажено.')
        except Exception as e:
            raise CommandError(f'Помилка під час читання CSV-файлу: {e}')

        # Очищення та обробка даних
        df.dropna(subset=['product_name'], inplace=True)

        # Змінено: Явно перетворюємо колонки на числові після завантаження
        for col in ['carbohydrates_100g', 'energy-kcal_100g', 'proteins_100g', 'fat_100g']:
            if col in df.columns:  # Перевіряємо, чи колонка існує
                df[col] = pd.to_numeric(df[col], errors='coerce')  # Перетворюємо на число, помилки в NaN

        df.fillna({  # Тепер NaN, створені to_numeric, будуть заповнені нулями
            'carbohydrates_100g': 0.0,
            'energy-kcal_100g': 0.0,
            'proteins_100g': 0.0,
            'fat_100g': 0.0
        }, inplace=True)

        # Перейменовуємо колонки для відповідності моделі Food
        df.rename(columns={
            'product_name': 'name',
            'categories_en': 'category',
            'carbohydrates_100g': 'carbs',
            'energy-kcal_100g': 'calories',
            'proteins_100g': 'protein',
            'fat_100g': 'fats'
        }, inplace=True)

        # Обмежуємо кількість продуктів, якщо вказано ліміт
        if limit:
            df = df.head(limit)
            self.stdout.write(self.style.WARNING(f'Імпорт обмежено до {limit} продуктів.'))

        # Зберігаємо унікальні категорії
        unique_categories = df['category'].apply(
            lambda x: str(x).split(',')[0].strip() if pd.notna(x) else 'Невідомо').dropna().unique()

        for category_name in unique_categories:
            if category_name:
                category, created = FoodCategory.objects.get_or_create(name=category_name)
                if created:
                    self.stdout.write(f'Створено категорію: {category.name}')

        # Імпортуємо продукти
        imported_count = 0
        skipped_count = 0

        # Перевіряємо, чи колонка 'product_name_uk' існує в DataFrame
        has_uk_name_col = 'product_name_uk' in df.columns

        for index, row in df.iterrows():
            # Визначаємо назву продукту: спочатку українська, потім англійська
            product_name = ''
            if has_uk_name_col and pd.notna(row['product_name_uk']) and str(row['product_name_uk']).strip() != '':
                product_name = str(row['product_name_uk']).strip()
            elif pd.notna(row['name']) and str(row['name']).strip() != '':
                product_name = str(row['name']).strip()

            if not product_name:
                skipped_count += 1
                continue

            category_name = str(row['category']).split(',')[0].strip() if pd.notna(row['category']) else 'Невідомо'
            if not category_name:
                category_name = 'Невідомо'

            try:
                category = FoodCategory.objects.get(name=category_name)
            except FoodCategory.DoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f'Помилка: Категорія "{category_name}" не знайдена для продукту "{product_name}". Пропускаю.'))
                skipped_count += 1
                continue

            food, created = Food.objects.get_or_create(
                name=product_name,
                carbs=row['carbs'],
                calories=row['calories'],
                protein=row['protein'],
                fats=row['fats'],
                defaults={'category': category}
            )
            if created:
                imported_count += 1

        self.stdout.write(self.style.SUCCESS(f'Успішно імпортовано {imported_count} нових продуктів.'))
        if skipped_count > 0:
            self.stdout.write(self.style.WARNING(
                f'Пропущено {skipped_count} продуктів через помилки (деякі могли мати порожню назву або відсутню категорію).'))
        self.stdout.write(self.style.SUCCESS('Імпорт завершено.'))
