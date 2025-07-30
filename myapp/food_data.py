# food_data.py (або можна вставити безпосередньо в команду імпорту)

FOOD_DATA = [
    # --- Овочі та Фрукти ---
    {
        'name': 'Яблуко',
        'category': 'Фрукти',
        'carbs': 14.0, 'calories': 52.0, 'protein': 0.3, 'fats': 0.2
    },
    {
        'name': 'Банан',
        'category': 'Фрукти',
        'carbs': 23.0, 'calories': 89.0, 'protein': 1.1, 'fats': 0.3
    },
    {
        'name': 'Огірок',
        'category': 'Овочі',
        'carbs': 3.6, 'calories': 15.0, 'protein': 0.7, 'fats': 0.1
    },
    {
        'name': 'Помідор',
        'category': 'Овочі',
        'carbs': 3.9, 'calories': 18.0, 'protein': 0.9, 'fats': 0.2
    },
    {
        'name': 'Морква',
        'category': 'Овочі',
        'carbs': 9.6, 'calories': 41.0, 'protein': 0.9, 'fats': 0.2
    },
    {
        'name': 'Картопля',
        'category': 'Овочі',
        'carbs': 17.0, 'calories': 77.0, 'protein': 2.0, 'fats': 0.1
    },

    # --- Зернові та Бобові ---
    {
        'name': 'Гречка',
        'category': 'Зернові',
        'carbs': 71.5, 'calories': 343.0, 'protein': 13.3, 'fats': 3.4
    },
    {
        'name': 'Рис білий',
        'category': 'Зернові',
        'carbs': 80.0, 'calories': 360.0, 'protein': 7.0, 'fats': 0.7
    },
    {
        'name': 'Вівсянка',
        'category': 'Зернові',
        'carbs': 66.0, 'calories': 389.0, 'protein': 16.9, 'fats': 6.9
    },
    {
        'name': 'Сочевиця',
        'category': 'Бобові',
        'carbs': 20.1, 'calories': 116.0, 'protein': 9.0, 'fats': 0.4
    },
    {
        'name': 'Квасоля',
        'category': 'Бобові',
        'carbs': 21.0, 'calories': 127.0, 'protein': 8.0, 'fats': 0.5
    },

    # --- М'ясо та Риба ---
    {
        'name': 'Куряче філе',
        'category': 'М\'ясо',
        'carbs': 0.0, 'calories': 165.0, 'protein': 31.0, 'fats': 3.6
    },
    {
        'name': 'Яловичина (м\'якоть)',
        'category': 'М\'ясо',
        'carbs': 0.0, 'calories': 250.0, 'protein': 26.0, 'fats': 15.0
    },
    {
        'name': 'Лосось',
        'category': 'Риба',
        'carbs': 0.0, 'calories': 208.0, 'protein': 20.0, 'fats': 13.0
    },
    {
        'name': 'Тунець консервований (у власному соку)',
        'category': 'Риба',
        'carbs': 0.0, 'calories': 116.0, 'protein': 25.0, 'fats': 1.0
    },

    # --- Молочні продукти та Яйця ---
    {
        'name': 'Молоко 2.5%',
        'category': 'Молочні продукти',
        'carbs': 4.7, 'calories': 53.0, 'protein': 3.0, 'fats': 2.5
    },
    {
        'name': 'Творог 5%',
        'category': 'Молочні продукти',
        'carbs': 3.0, 'calories': 121.0, 'protein': 18.0, 'fats': 5.0
    },
    {
        'name': 'Йогурт натуральний',
        'category': 'Молочні продукти',
        'carbs': 4.7, 'calories': 61.0, 'protein': 3.5, 'fats': 3.3
    },
    {
        'name': 'Сир твердий (Гауда)',
        'category': 'Молочні продукти',
        'carbs': 1.3, 'calories': 356.0, 'protein': 25.0, 'fats': 27.0
    },
    {
        'name': 'Яйце куряче',
        'category': 'Яйця',
        'carbs': 0.6, 'calories': 155.0, 'protein': 13.0, 'fats': 11.0
    },

    # --- Горіхи та Насіння ---
    {
        'name': 'Мигдаль',
        'category': 'Горіхи та насіння',
        'carbs': 21.6, 'calories': 579.0, 'protein': 21.2, 'fats': 49.9
    },
    {
        'name': 'Волоський горіх',
        'category': 'Горіхи та насіння',
        'carbs': 13.7, 'calories': 654.0, 'protein': 15.2, 'fats': 65.2
    },

    # --- Готові продукти та Напої ---
    {
        'name': 'Хліб пшеничний',
        'category': 'Хлібобулочні вироби',
        'carbs': 49.0, 'calories': 264.0, 'protein': 9.0, 'fats': 3.0
    },
    {
        'name': 'Макарони (сухі)',
        'category': 'Зернові',
        'carbs': 75.0, 'calories': 371.0, 'protein': 13.0, 'fats': 1.5
    },
    {
        'name': 'Кетчуп',
        'category': 'Соуси',
        'carbs': 23.0, 'calories': 100.0, 'protein': 1.0, 'fats': 0.1
    },
    {
        'name': 'Майонез',
        'category': 'Соуси',
        'carbs': 2.0, 'calories': 680.0, 'protein': 1.0, 'fats': 75.0
    },
    {
        'name': 'Цукор',
        'category': 'Підсолоджувачі',
        'carbs': 100.0, 'calories': 400.0, 'protein': 0.0, 'fats': 0.0
    },
    {
        'name': 'Мед',
        'category': 'Підсолоджувачі',
        'carbs': 82.0, 'calories': 304.0, 'protein': 0.3, 'fats': 0.0
    },
    {
        'name': 'Чай чорний (без цукру)',
        'category': 'Напої',
        'carbs': 0.0, 'calories': 1.0, 'protein': 0.0, 'fats': 0.0
    },
    {
        'name': 'Кава чорна (без цукру)',
        'category': 'Напої',
        'carbs': 0.0, 'calories': 2.0, 'protein': 0.1, 'fats': 0.0
    },
    {
        'name': 'Сік апельсиновий',
        'category': 'Напої',
        'carbs': 10.0, 'calories': 45.0, 'protein': 0.7, 'fats': 0.1
    },
    {
        'name': 'Піца (середня, м\'ясна)',
        'category': 'Готові страви',
        'carbs': 25.0, 'calories': 266.0, 'protein': 11.0, 'fats': 12.0
    },
    {
        'name': 'Бургер (середній)',
        'category': 'Готові страви',
        'carbs': 28.0, 'calories': 295.0, 'protein': 17.0, 'fats': 14.0
    },
    {
        'name': 'Картопля фрі',
        'category': 'Готові страви',
        'carbs': 41.0, 'calories': 312.0, 'protein': 3.4, 'fats': 15.0
    },
    {
        'name': 'Шоколад молочний',
        'category': 'Солодощі',
        'carbs': 59.0, 'calories': 535.0, 'protein': 8.0, 'fats': 30.0
    },
    {
        'name': 'Морозиво пломбір',
        'category': 'Солодощі',
        'carbs': 21.0, 'calories': 207.0, 'protein': 3.5, 'fats': 12.0
    },
    {
        'name': 'Газована вода (Кока-Кола)',
        'category': 'Напої',
        'carbs': 10.6, 'calories': 42.0, 'protein': 0.0, 'fats': 0.0
    },
    {
        'name': 'Пиво світле',
        'category': 'Напої',
        'carbs': 3.6, 'calories': 43.0, 'protein': 0.5, 'fats': 0.0
    },
    {
        'name': 'Вино червоне сухе',
        'category': 'Напої',
        'carbs': 2.6, 'calories': 85.0, 'protein': 0.1, 'fats': 0.0
    },
    {
        'name': 'Чіпси картопляні',
        'category': 'Снеки',
        'carbs': 53.0, 'calories': 536.0, 'protein': 6.0, 'fats': 34.0
    },
    {
        'name': 'Печиво вівсяне',
        'category': 'Хлібобулочні вироби',
        'carbs': 65.0, 'calories': 437.0, 'protein': 7.0, 'fats': 17.0
    },
    {
        'name': 'Суші (рол Філадельфія)',
        'category': 'Готові страви',
        'carbs': 28.0, 'calories': 180.0, 'protein': 8.0, 'fats': 4.0
    },
    {
        'name': 'Салат Цезар (з куркою)',
        'category': 'Готові страви',
        'carbs': 8.0, 'calories': 150.0, 'protein': 12.0, 'fats': 8.0
    },
    {
        'name': 'Суп курячий',
        'category': 'Готові страви',
        'carbs': 5.0, 'calories': 60.0, 'protein': 5.0, 'fats': 3.0
    },
    {
        'name': 'Борщ',
        'category': 'Готові страви',
        'carbs': 10.0, 'calories': 70.0, 'protein': 2.0, 'fats': 3.0
    },
    {
        'name': 'Вареники з картоплею',
        'category': 'Готові страви',
        'carbs': 25.0, 'calories': 150.0, 'protein': 5.0, 'fats': 4.0
    },
    {
        'name': 'Плов',
        'category': 'Готові страви',
        'carbs': 20.0, 'calories': 180.0, 'protein': 7.0, 'fats': 8.0
    },
    {
        'name': 'Каша рисова на молоці',
        'category': 'Готові страви',
        'carbs': 15.0, 'calories': 100.0, 'protein': 3.0, 'fats': 3.0
    },
    {
        'name': 'Омлет з сиром',
        'category': 'Готові страви',
        'carbs': 2.0, 'calories': 150.0, 'protein': 10.0, 'fats': 12.0
    },
    {
        'name': 'Сендвіч з куркою',
        'category': 'Готові страви',
        'carbs': 25.0, 'calories': 250.0, 'protein': 15.0, 'fats': 10.0
    },
    {
        'name': 'Піца (вегетаріанська)',
        'category': 'Готові страви',
        'carbs': 28.0, 'calories': 220.0, 'protein': 9.0, 'fats': 8.0
    },
    {
        'name': 'Лазанья',
        'category': 'Готові страви',
        'carbs': 20.0, 'calories': 220.0, 'protein': 12.0, 'fats': 10.0
    },
    {
        'name': 'Млинці з м\'ясом',
        'category': 'Готові страви',
        'carbs': 18.0, 'calories': 200.0, 'protein': 10.0, 'fats': 10.0
    },
    {
        'name': 'Салат Олів\'є',
        'category': 'Готові страви',
        'carbs': 10.0, 'calories': 180.0, 'protein': 5.0, 'fats': 14.0
    },
    {
        'name': 'Шаурма',
        'category': 'Готові страви',
        'carbs': 30.0, 'calories': 350.0, 'protein': 20.0, 'fats': 18.0
    },
    {
        'name': 'Хот-дог',
        'category': 'Готові страви',
        'carbs': 25.0, 'calories': 280.0, 'protein': 10.0, 'fats': 15.0
    },
    {
        'name': 'Круасан',
        'category': 'Хлібобулочні вироби',
        'carbs': 45.0, 'calories': 407.0, 'protein': 8.0, 'fats': 22.0
    },
    {
        'name': 'Еклери',
        'category': 'Солодощі',
        'carbs': 30.0, 'calories': 250.0, 'protein': 5.0, 'fats': 15.0
    },
    {
        'name': 'Торт (шматок)',
        'category': 'Солодощі',
        'carbs': 50.0, 'calories': 350.0, 'protein': 4.0, 'fats': 15.0
    },
    {
        'name': 'Каша гречана з грибами',
        'category': 'Готові страви',
        'carbs': 18.0, 'calories': 120.0, 'protein': 5.0, 'fats': 4.0
    },
    {
        'name': 'Котлета по-київськи',
        'category': 'Готові страви',
        'carbs': 15.0, 'calories': 350.0, 'protein': 20.0, 'fats': 25.0
    },
    {
        'name': 'Деруни',
        'category': 'Готові страви',
        'carbs': 25.0, 'calories': 220.0, 'protein': 4.0, 'fats': 12.0
    },
    {
        'name': 'Сирники',
        'category': 'Готові страви',
        'carbs': 20.0, 'calories': 180.0, 'protein': 10.0, 'fats': 8.0
    },
    {
        'name': 'Омлет з овочами',
        'category': 'Готові страви',
        'carbs': 5.0, 'calories': 120.0, 'protein': 8.0, 'fats': 8.0
    },
    {
        'name': 'Мюслі з молоком',
        'category': 'Сніданки',
        'carbs': 20.0, 'calories': 150.0, 'protein': 5.0, 'fats': 5.0
    },
    {
        'name': 'Гранола',
        'category': 'Снеки',
        'carbs': 60.0, 'calories': 470.0, 'protein': 10.0, 'fats': 20.0
    },
    {
        'name': 'Сухофрукти (мікс)',
        'category': 'Фрукти',
        'carbs': 70.0, 'calories': 280.0, 'protein': 3.0, 'fats': 0.5
    },
    {
        'name': 'Хумус',
        'category': 'Соуси',
        'carbs': 15.0, 'calories': 166.0, 'protein': 8.0, 'fats': 10.0
    },
    {
        'name': 'Лаваш',
        'category': 'Хлібобулочні вироби',
        'carbs': 50.0, 'calories': 250.0, 'protein': 8.0, 'fats': 1.0
    },
    {
        'name': 'Фалафель',
        'category': 'Готові страви',
        'carbs': 25.0, 'calories': 333.0, 'protein': 13.0, 'fats': 18.0
    },
    {
        'name': 'Пончик',
        'category': 'Солодощі',
        'carbs': 35.0, 'calories': 250.0, 'protein': 4.0, 'fats': 12.0
    },
    {
        'name': 'Круасан з шоколадом',
        'category': 'Хлібобулочні вироби',
        'carbs': 50.0, 'calories': 450.0, 'protein': 9.0, 'fats': 25.0
    },
    {
        'name': 'Енергетичний батончик',
        'category': 'Снеки',
        'carbs': 30.0, 'calories': 150.0, 'protein': 5.0, 'fats': 5.0
    },
    {
        'name': 'Протеїновий батончик',
        'category': 'Снеки',
        'carbs': 20.0, 'calories': 200.0, 'protein': 20.0, 'fats': 8.0
    },
    {
        'name': 'Смузі фруктовий',
        'category': 'Напої',
        'carbs': 25.0, 'calories': 120.0, 'protein': 2.0, 'fats': 1.0
    },
]
