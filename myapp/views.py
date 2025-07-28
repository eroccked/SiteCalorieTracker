from django.shortcuts import render, redirect, get_object_or_404
from .models import Food, Consume
from django.contrib.auth.decorators import login_required
from datetime import datetime, date  # Додано date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.utils import timezone
from django.views.decorators.http import require_POST


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
            return redirect(f'/index/?selected_date={selected_date.strftime("%Y-%m-%d")}')
        except ValueError:
            print(f"Помилка: Недійсний ID їжі '{food_id}'")
            pass

    foods = Food.objects.all()
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

    return render(request, 'myapp/index.html', {
        'foods': foods,
        'meals_data': meals_data,
        'total_carbs': total_carbs,
        'total_calories': total_calories,
        'total_protein': total_protein,
        'total_fats': total_fats,
        'selected_date': selected_date,  # Передаємо обрану дату в шаблон
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
        return redirect(f'/index/?selected_date={selected_date_str}')
    return redirect('index')
