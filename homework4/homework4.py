# Цикл для ввода чисел
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

# Подсчет четных и нечетных элементов
even_count = sum(1 for num in numbers if num % 2 == 0)
odd_count = sum(1 for num in numbers if num % 2 != 0)

# Вывод результатов
print("Количество четных элементов:", even_count)
print("Количество нечетных элементов:", odd_count)
