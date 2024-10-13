# Переменная для подсчета вызовов функций
calls = 0

def count_calls():
    """Функция для увеличения счетчика вызовов."""
    global calls
    calls += 1

def string_info(string):
    """Возвращает кортеж (длина строки, строка в верхнем регистре, строка в нижнем регистре)."""
    count_calls()  # Увеличиваем количество вызовов
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    """Проверяет, содержится ли строка в списке, игнорируя регистр."""
    count_calls()  # Увеличиваем количество вызовов
    return string.lower() in (item.lower() for item in list_to_search)

# Примеры вызова функций. Вы можете вызывать их произвольное количество раз
if __name__ == "__main__":
    print(string_info("Hello, World!"))  # Пример вызова string_info
    print(is_contains("URbaN", ["urban", "town", "city"]))  # Пример вызова is_contains
    print(string_info("Python Programming"))  # Еще один вызов string_info
    print(is_contains("Python", ["Java", "C++", "Python"]))  # Еще один вызов is_contains

    # Вывод количества вызовов функций
    print("Общее количество вызовов функций:", calls)


