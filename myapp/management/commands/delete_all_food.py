from django.core.management.base import BaseCommand, CommandError
from myapp.models import Food # Імпортуємо модель Food

class Command(BaseCommand):
    help = 'Видаляє всі записи з моделі Food.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Починаю видалення всіх продуктів з бази даних...'))

        try:
            num_deleted, _ = Food.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f'Успішно видалено {num_deleted} продуктів.'))
        except Exception as e:
            raise CommandError(f'Виникла помилка під час видалення продуктів: {e}')

