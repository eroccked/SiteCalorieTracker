from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    # Додаємо цей метод, щоб імпортувати сигнали при запуску додатку
    def ready(self):
        import myapp.signals  # noqa: F401
        # noqa: F401 - це коментар для лінтерів, щоб вони не скаржилися на невикористаний імпорт
