import random

# Лотерейный билет
ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

# Функция для выбора чисел пользователем
def user_selection():
    user_numbers = []
    for i in range(len(ticket)):
        while True:
            try:
                number = int(input(f"Выберите число из строки {i + 1} {ticket[i]}: "))
                if number in ticket[i]:
                    user_numbers.append(number)
                    break
                else:
                    print("Ошибка: число не из данной строки. Попробуйте снова.")
            except ValueError:
                print("Ошибка: введите корректное целое число.")
    return user_numbers

# Функция для случайного выбора чисел
def random_selection():
    random_numbers = []
    for row in ticket:
        random_numbers.append(random.choice(row))
    return random_numbers

# Основная логика приложения
def lottery_app():
    print("Добро пожаловать в лотерею!")
    
    # Выбор пользователем
    user_numbers = user_selection()
    print("Ваши выбранные числа:", user_numbers)

    # Случайный выбор
    random_numbers = random_selection()
    print("Случайно выбранные числа:", random_numbers)

    # Подсчет совпадений
    matches = set(user_numbers) & set(random_numbers)
    print("Совпадения:", matches)
    print("Количество совпадений:", len(matches))

# Запуск приложения
lottery_app()
