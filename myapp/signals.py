from django.db.models.signals import post_save  # Імпортуємо сигнал, який надсилається після збереження моделі
from django.contrib.auth.models import User  # Імпортуємо стандартну модель User
from django.dispatch import receiver  # Імпортуємо декоратор для реєстрації ресивера

from .models import UserProfile


# Декоратор @receiver вказує, що функція create_user_profile буде "слухати" сигнал post_save
# від моделі User.
# sender=User: Ми слухаємо сигнали тільки від моделі User.
# created=True: Ця функція буде викликана тільки тоді, коли об'єкт User був щойно створений (не оновлений).
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Якщо користувач був щойно створений, створюємо для нього UserProfile
        UserProfile.objects.create(user=instance)


# Декоратор @receiver для збереження UserProfile при збереженні User
# Це потрібно, якщо ви редагуєте користувача в адмінці і хочете, щоб зміни в профілі теж збереглися.
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Перевіряємо, чи існує профіль, перш ніж намагатися його зберегти
    # Це важливо, якщо профіль ще не був створений (наприклад, при першому запуску після міграцій)
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()
