# Проект FitLife - MVP версия 2.0

# | Спасибо за обратную связь, добавил проверку на корректность ввода.
# | Проверку по весу и росту объединил в одну функцию - убрал дублирование.
# | Было интересно разобраться и посмотреть что еще можно сделать.


WATER_PER_KG = 30
ML_PER_LITER = 1000


# 1. Запрос имени и проверка его
def get_user_name():
    """Запрашивает имя и проверяет корректность ввода"""
    first_attempt = True

    while True:
        if first_attempt:
            user_name = input('Как Вас зовут? ')
        else:
            user_name = input('Введите имя повторно: ')

        user_name = user_name.strip()

        if user_name == '':
            print('Ошибка! Имя не может быть пустым.')
            first_attempt = False
            continue

        if not user_name.isalpha():
            print('Ошибка! Имя должно содержать только буквы.')
            first_attempt = False
            continue

        return user_name


# 2. Запрос возраста и проверка его
def get_user_age():
    """Запрашивает возраст и проверяет корректность ввода"""
    first_attempt = True

    while True:
        if first_attempt:
            user_age = input('Сколько Вам лет? ')
        else:
            user_age = input('Введите возраст повторно: ')

        user_age = user_age.strip()

        if not user_age.isdigit():
            print('Ошибка! Число должно быть целым числом.')
            first_attempt = False
            continue

        user_age = int(user_age)

        if user_age <= 0 or user_age >= 100:
            print('Ошибка! Введите возраст от 0 до 110 лет.')
            first_attempt = False
            continue

        return user_age


# 3. Запрос веса (в кг, например 25.4) / / роста (в метрах, например 1.75)
def get_weight_or_height(question, repeat_question):
    """Запрашивает данные по весу или росту и проверяет корректность ввода"""
    first_attempt = True

    while True:
        if first_attempt:
            value = input(question)
        else:
            value = input(repeat_question)

        value = value.strip().replace(',', '.')

        try:
            value = float(value)
        except ValueError:
            print('Ошибка! Повторите ввод')
            first_attempt = False
            continue

        if value < 1 or value > 400:
            print('Ошибка! Повторите ввод')
            first_attempt = False
            continue

        return value


# 4. Расчет bmi (Индекс массы тела)
def calc_bmi(user_weight, user_height):
    """Считает индекс массы тела и округляет до одного знака после запятой."""
    return round(user_weight / (user_height ** 2), 1)


# 5. Подсчет воды: вес * 30 мл
def calc_water(user_weight):
    """Считает норму воды в литрах: 30 мл на каждый кг веса."""
    return round(user_weight * WATER_PER_KG / ML_PER_LITER, 1)


# 6. Основная программа
def main():
    """Запускает основную программу"""
    # Блок знакомства
    user_name = get_user_name()
    user_age = get_user_age()

    # Блок сбора данных
    user_weight = get_weight_or_height(
        'Напишите вес в килограммах (пример: 25.4) ',
        'Повторите ввод веса в килограммах (пример: 25.4) '
    )

    user_height = get_weight_or_height(
        'Напишите рост в метрах (пример 1.75) ',
        'Повторите ввод роста в метрах (пример 1.75) '
    )

    # Блок расчета
    bmi = calc_bmi(user_weight, user_height)
    water = calc_water(user_weight)

    # Блок вывода результата
    print(f'Отчет для пользователя: {user_name} ({user_age} лет)')
    print(f'Твой Индекс Массы Тела: {bmi}')
    print(f'Рекомендуемая норма воды: {water} л. в день\n')
    print("Расчет окончен. Будьте здоровы!")


# 7. Запуск программы
if __name__ == '__main__':
    main()
