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
    # Список для хранения элементов, которые больше предыдущего
    greater_than_previous = []

    # Проход по списку, начиная со второго элемента
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            greater_than_previous.append(numbers[i])

    # Вывод результата
    print("Элементы, которые больше предыдущего элемента:", greater_than_previous)
else:
    print("Список пуст.")
