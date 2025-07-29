from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import FoodCategory, Food, Consume, UserProfile

# Реєструємо існуючі моделі
admin.site.register(FoodCategory)
admin.site.register(Food)
admin.site.register(Consume)

# Клас для вбудованого відображення UserProfile в адмінці User
class UserProfileInline(admin.StackedInline): # StackedInline для більш зручного відображення полів
    model = UserProfile
    can_delete = False # Забороняємо видаляти профіль окремо від користувача
    verbose_name_plural = 'Профіль користувача' # Назва секції в адмінці

# Перевизначаємо стандартний UserAdmin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,) # Додаємо UserProfileInline до стандартного UserAdmin

# Відреєстровуємо стандартний UserAdmin, щоб потім зареєструвати наш власний
admin.site.unregister(User)
admin.site.register(User, UserAdmin) # Реєструємо модель User з нашим кастомним UserAdmin
