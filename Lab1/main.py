import random
import time

random.seed(time.time())

# Функція заперечення
def NOT(a):
    return 1 - a

# Функція кон'юнкції
def AND(a, b):
    return min(a, b)

# Функція диз'юнкції
def OR(a, b):
    return max(a, b)

# Функція імплікації (a імплікує b)
def IMP(a, b):
    return max(1 - a, b)

# Функція еквівалентності (a тоді і тільки тоді, коли b)
def EQU(a, b):
    return 1 if a == b else 0

# 5 варіант
def complex_statement(A, B, C):
    part1 = AND(A, OR(B, NOT(C)))  # A AND (B OR NOT(C))
    part2 = OR(NOT(A), AND(B, C))  # NOT(A) OR (B AND C)
    result = EQU(part1, part2)     # (part1) EQU (part2)
    return result

# Генерація 10 різних значень A, B, C (випадкові значення від 0 до 1)
def generate_truth_values():
    return [(random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)) for _ in range(10)]

# Побудова таблиці істинності
def build_truth_table() -> list:
    truth_values = generate_truth_values()
    table = []

    for A, B, C in truth_values:
        result = complex_statement(A, B, C)
        table.append((A, B, C, result))

    return table

# Виведення таблиці істинності
def print_truth_table():
    truth_table = build_truth_table()
    print("f = |A AND (B OR (NOT(C))) EQU |NOT(A) OR (B AND C)|")
    print(f"{'A':>3} {'B':>4} {'C':>4} {'f':>4}")

    for row in truth_table:
        A, B, C, result = row
        print(f"{A:.2f} {B:.2f} {C:.2f} {result:.2f}")


# Виклик функції для побудови та виведення таблиці істинності
print_truth_table()
