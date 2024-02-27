def caching_fibonacci():
    # Створити порожній словник для кешу
    cache = {}

    def fibonacci(n):
        # Якщо число менше або дорівнює 0, повернути 0
        if n <= 0:
            return 0
        # Якщо число дорівнює 1, повернути 1
        elif n == 1:
            return 1
        # Якщо число вже є в кеші, повернути його значення
        elif n in cache:
            return cache[n]
        # Інакше обчислити число Фібоначчі та зберегти його в кеші
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    # Повернути функцію fibonacci
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610

