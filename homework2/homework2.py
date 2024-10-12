# Функция для проверки, является ли введённое значение числом
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Ввод чисел a и b с проверкой на корректность
while True:
    a_input = input("Введите число a: ")
    if is_number(a_input):
        a = int(a_input)
        break
    else:
        print("Ошибка: введите целое число.")

while True:
    b_input = input("Введите число b: ")
    if is_number(b_input):
        b = int(b_input)
        break
    else:
        print("Ошибка: введите целое число.")

# Создание списка квадратов целых чисел между a и b
squares = [i**2 for i in range(a, b + 1)]

# Вывод результата
print("Список квадратов целых чисел между", a, "и", b, ":", squares)

