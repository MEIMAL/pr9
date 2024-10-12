# Инициализация пустого списка для хранения чисел
numbers = []

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

# Вывод нечетных элементов списка
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Нечетные элементы списка:", odd_numbers)
