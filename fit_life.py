# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
ML_PER_LITER = 1000

# 1. Знакомство
user_name = input('Как вас зовут? ')
user_age = int(input('Сколько вам лет? '))


# 2. Сбор данных: вес (в кг, например 25.4), рост (в метрах, например 1.75)
user_weight = float(input('Напишите свой вес в килограммах (пример: 25.4) '))
user_height = float(input('Напишите свой рост в метрах (пример 1.75) '))


# 3. Рассчитай bmi (Индекс массы тела)
def calс_bmi(user_weight, user_height):
    """Считает индекс массы тела и округляет до одного знака после запятой."""
    return round(user_weight / (user_height ** 2), 1)


# 4. Подсчет воды: вес * 30 мл
def calс_water(user_weight):
    """"Считает норму воды в литрах: 30 мл на каждый кг веса."""
    return round(user_weight * WATER_PER_KG / ML_PER_LITER, 1)


# 5. Вызов функций
bmi = calс_bmi(user_weight, user_height)
water = calс_water(user_weight)

# 6. Вывод результата
print(f'Отчет для пользователя: {user_name} ({user_age} лет)')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water} л. в день\n')
print("Расчет окончен. Будьте здоровы!")
