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
    # Сохранение последнего элемента
    last_element = numbers[-1]
    
    # Сдвиг элементов вправо
    for i in range(len(numbers) - 1, 0, -1):
        numbers[i] = numbers[i - 1]
    
    # Установка последнего элемента на первое место
    numbers[0] = last_element

    # Вывод результата
    print("Список после циклического сдвига вправо:", numbers)
else:
    print("Список пуст.")
