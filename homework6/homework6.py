# Инициализация пустого списка для хранения чисел
numbers = []

# Запрос ввода чисел от пользователя
while True:
    user_input = input("Введите число (или 'end' для завершения): ")
    if user_input.lower() == 'end':
        break
    try:
        # Преобразование введенного значения в целое число
        number = int(user_input)
        numbers.append(number)  # Добавление числа в список
    except ValueError:
        print("Ошибка: введите корректное целое число.")

# Проверка, что список не пустой
if numbers:
    # Находим индексы минимального и максимального элементов
    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))

    # Меняем местами минимальный и максимальный элементы
    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

    # Вывод результата
    print("Список после замены:", numbers)
else:
    print("Список пуст.")
