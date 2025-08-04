from django.shortcuts import render, redirect, get_object_or_404
from .models import Food, Consume, UserProfile  # Імпортуємо UserProfile
from .forms import UserProfileForm  # Імпортуємо нашу форму профілю
from django.contrib.auth.decorators import login_required
from datetime import datetime, date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.utils import timezone
from django.views.decorators.http import require_POST
import re
from django.http import JsonResponse  # <--- Додано для повернення JSON відповідей


@login_required
def index(request):
    selected_date_str = request.GET.get('selected_date')
    if selected_date_str:
        try:
            selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d').date()
        except ValueError:
            selected_date = timezone.now().date()
    else:
        selected_date = timezone.now().date()

    if request.method == 'POST':
        food_id = request.POST['food_consumed']
        meal_type = request.POST['meal_type']
        weight = float(request.POST.get('weight', 100))

        try:
            food = get_object_or_404(Food, id=food_id)
            Consume.objects.create(user=request.user, food=food, meal_type=meal_type, date=timezone.now().date(),
                                   weight=weight)
            return redirect(f'/?selected_date={selected_date.strftime("%Y-%m-%d")}')
        except ValueError:
            print(f"Помилка: Недійсний ID їжі '{food_id}'")
            pass

    # Змінено: foods більше не завантажується тут.
    # foods = Food.objects.all() # <--- Цей рядок видалено або закоментовано

    consumed_food = Consume.objects.filter(user=request.user, date=selected_date).select_related('food')

    meals = {
        'Сніданок': consumed_food.filter(meal_type='breakfast'),
        'Обід': consumed_food.filter(meal_type='lunch'),
        'Вечеря': consumed_food.filter(meal_type='dinner'),
        'Перекус': consumed_food.filter(meal_type='snack'),
    }

    def calculate_nutrients(items):
        total_carbs = 0
        total_calories = 0
        total_protein = 0
        total_fats = 0

        for item in items:
            total_carbs += item.carbs_weighted
            total_calories += item.calories_weighted
            total_protein += item.protein_weighted
            total_fats += item.fats_weighted

        return total_carbs, total_calories, total_protein, total_fats

    meals_data = {}
    for meal_title, items in meals.items():
        carbs, calories, protein, fats = calculate_nutrients(items)
        meals_data[meal_title] = {
            'items': items,
            'carbs': carbs,
            'calories': calories,
            'protein': protein,
            'fats': fats,
        }

    total_carbs = sum(data['carbs'] for data in meals_data.values())
    total_calories = sum(data['calories'] for data in meals_data.values())
    total_protein = sum(data['protein'] for data in meals_data.values())
    total_fats = sum(data['fats'] for data in meals_data.values())

    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    mobile_pat = re.compile(r'android|iphone|ipad|ipod|blackberry|windows phone|iemobile|opera mini', re.I)

    # Оскільки ми більше не працюємо з мобільною версією, можна спростити
    # if mobile_pat.search(user_agent):
    #     template_name = 'myapp/index_mobile.html'
    # else:
    template_name = 'myapp/index.html'

    return render(request, template_name, {
        # 'foods': foods, # <--- foods більше не передається
        'meals_data': meals_data,
        'total_carbs': total_carbs,
        'total_calories': total_calories,
        'total_protein': total_protein,
        'total_fats': total_fats,
        'selected_date': selected_date,
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@require_POST
@login_required
def delete_consume(request, consume_id):
    item = get_object_or_404(Consume, id=consume_id, user=request.user)
    item.delete()
    selected_date_str = request.GET.get('selected_date')
    if selected_date_str:
        return redirect(f'/?selected_date={selected_date_str}')
    return redirect('/')


# Нова в'юшка для відображення профілю користувача
@login_required
def profile_view(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'myapp/profile.html', {'user_profile': user_profile})


# Нова в'юшка для редагування профілю користувача
@login_required
def profile_edit(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'myapp/profile_edit.html', {'form': form, 'user_profile': user_profile})


# Нова AJAX-в'юшка для пошуку продуктів
def food_search_ajax(request):
    query = request.GET.get('q', '')  # Отримуємо пошуковий запит

    if query:
        # Шукаємо продукти, назва яких містить запит (без урахування регістру)
        # Обмежуємо кількість результатів, щоб не перевантажувати фронтенд
        foods = Food.objects.filter(name__icontains=query).values('id', 'name')[:50]  # Беремо до 50 результатів
    else:
        foods = []  # Якщо запит порожній, повертаємо порожній список

    # Перетворюємо QuerySet на список словників для JSON
    food_list = list(foods)
    return JsonResponse({'foods': food_list})
