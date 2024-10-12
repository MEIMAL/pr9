import re

# Функция для разбора email
def parse_email(email):
    # Регулярное выражение для разбора email, чтобы он не начинался с цифры
    pattern = r'^[a-zA-Z][\w.-]*@(.+)'
    match = re.match(pattern, email)
    
    if match:
        username = email.split('@')[0]  # Имя пользователя
        domain = match.group(1)          # Доменное имя
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
        print("Ошибка: введен некорректный email. Email не может начинаться с цифры.")

# Запуск приложения
if __name__ == "__main__":
    main()
