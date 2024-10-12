import re

# Функция для разбора email
def parse_email(email):
    # Регулярное выражение для разбора email
    pattern = r'([^@]+)@(.+)'
    match = re.match(pattern, email)
    
    if match:
        username = match.group(1)  # Имя пользователя
        domain = match.group(2)     # Доменное имя
        return username, domain
    else:
        return None, None

# Основная логика приложения
def main():
    email = input("Введите ваш email: ")
    username, domain = parse_email(email)
    
    if username and domain:
        print(f"Имя пользователя: {username}")
        print(f"Доменное имя: {domain}")
    else:
        print("Ошибка: введен некорректный email.")

# Запуск приложения
if __name__ == "__main__":
    main()
