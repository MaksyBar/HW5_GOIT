import re
from typing import Callable

def generator_numbers(text: str):
    # Використовуємо регулярний вираз для знаходження всіх дійсних чисел у тексті
    pattern = r'\b\d+\.\d+\b'
    # pattern = r"[-+]?\d+\.\d+|\d+"  # Пошук чисел з десятковою крапкою або цілих чисел
    for match in re.finditer(pattern, text):
        yield float(match.group())  # Повертаємо числа як генератор

def sum_profit(text: str, func: Callable):
    total_income = sum(func(text))  # Обчислюємо суму чисел, використовуючи генератор
    return round(total_income, 2)  # Округлюємо до двох знаків після коми

# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
