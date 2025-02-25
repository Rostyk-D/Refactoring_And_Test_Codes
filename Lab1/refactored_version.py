"""
Цей модуль містить клас для обчислення логічних операцій,
побудови таблиці істинності та виведення результатів.

Клас:
- LogicOperations: Містить методи для виконання логічних операцій та побудови таблиці істинності.
"""

import random
import time

class LogicOperations:
    """Клас для обчислення логічних операцій та побудови таблиці істинності."""

    def __init__(self):
        random.seed(time.time())

    # Функція заперечення (NOT)
    def not_operation(self, a):
        """Повертає 1 - a"""
        return 1 - a

    # Функція кон'юнкції (AND)
    def and_operation(self, a, b):
        """Повертає мінімум з a та b"""
        return min(a, b)

    # Функція диз'юнкції (OR)
    def or_operation(self, a, b):
        """Повертає максимум з a та b"""
        return max(a, b)

    # Функція імплікації (IMP)
    def imp_operation(self, a, b):
        """Повертає max(1 - a, b), що є імплікацією a до b"""
        return max(1 - a, b)

    # Функція еквівалентності (EQU)
    def equ_operation(self, a, b):
        """Повертає 1, якщо a еквівалентно b, інакше 0"""
        return 1 if a == b else 0

    # Функція для побудови складного логічного виразу
    def complex_statement(self, a, b, c):
        """Обчислює приклад: A AND (B OR NOT(C)) EQU NOT(A) OR (B AND C)"""
        part1 = self.and_operation(a, self.or_operation(b, self.not_operation(c)))
        part2 = self.or_operation(self.not_operation(a), self.and_operation(b, c))
        result = self.equ_operation(part1, part2)
        return result

    # Генерація 10 різних значень для A, B, C (випадкові значення від 0 до 1)
    def generate_truth_values(self):
        """Генерує 10 різних трійок значень A, B, C"""
        return [(random.randint(0, 1), random.randint(0, 1), random.randint(0, 1))
                for _ in range(10)]

    # Побудова таблиці істинності
    def build_truth_table(self) -> list:
        """Створює таблицю істинності для виразу"""
        truth_values = self.generate_truth_values()
        table = []

        for a, b, c in truth_values:
            result = self.complex_statement(a, b, c)
            table.append((a, b, c, result))

        return table

    # Виведення таблиці істинності
    def print_truth_table(self):
        """Виводить таблицю істинності"""
        truth_table = self.build_truth_table()
        print("f = |A AND (B OR (NOT(C))) EQU |NOT(A) OR (B AND C)|")
        print(f"{'A':>3} {'B':>4} {'C':>4} {'f':>4}")

        for row in truth_table:
            a, b, c, result = row
            print(f"{a:.2f} {b:.2f} {c:.2f} {result:.2f}")


# Виклик функції для побудови та виведення таблиці істинності
if __name__ == "__main__":
    logic_operations = LogicOperations()
    logic_operations.print_truth_table()
