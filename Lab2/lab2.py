import numpy as np
import random
import time
import matplotlib.pyplot as plt

# Ініціалізація генератора випадкових чисел на основі поточного часу
random.seed(time.time())

# Множини спеціальностей, характеристик і претендентів
X = ["менеджер", "програміст", "водій", "секретар"]
Y = ["гнучкість мислення", "критичне мислення", "концентрація уваги",
     "здорова пам'ять", "витривалість", "швидкість реакції рухів", "відповідальність"]
Z = ["Андрієнко", "Василенко", "Іваненко", "Дмитренко", "Петренко", "Романенко"]

# Функція для генерації випадкової матриці з використанням random
def generate_random_matrix(rows, cols):
    return np.array([[random.random() for _ in range(cols)] for _ in range(rows)])

# Генеруємо випадкові матриці нечіткого відношення S (спеціальності x характеристики)
S = generate_random_matrix(len(X), len(Y))

# Генеруємо випадкові матриці нечіткого відношення Q (характеристики x претенденти)
Q = generate_random_matrix(len(Y), len(Z))

# Функція для виконання композиції нечітких відношень
def fuzzy_composition(S, Q):
    XZ = np.zeros((S.shape[0], Q.shape[1]))
    for i in range(S.shape[0]):
        for j in range(Q.shape[1]):
            XZ[i, j] = np.max(np.minimum(S[i, :], Q[:, j]))
    return XZ

# Функція для виконання альтернативної мінімальної композиції нечітких відношень
def fuzzy_composition_minmax(S, Q):
    XZ = np.zeros((S.shape[0], Q.shape[1]))
    for i in range(S.shape[0]):
        for j in range(Q.shape[1]):
            XZ[i, j] = np.min(np.maximum(S[i, :], Q[:, j]))
    return XZ

# Обчислюємо композицію
result = fuzzy_composition(S, Q)
alt_result = fuzzy_composition_minmax(S, Q)

# Функція для побудови графіка матриці
def plot_matrix(matrix, x_labels, y_labels, title):
    fig, ax = plt.subplots(figsize=(14, 12))  #розмір графіка
    cax = ax.matshow(matrix, cmap='Blues')

    # Додати кольорову шкалу
    fig.colorbar(cax)

    # Підписи осі
    ax.set_xticks(np.arange(len(x_labels)))
    ax.set_yticks(np.arange(len(y_labels)))

    # Додати імена спеціальностей та претендентів
    ax.set_xticklabels(x_labels, fontsize=10, rotation=90, ha='right')
    ax.set_yticklabels(y_labels, fontsize=10)

    # Назва графіка
    plt.title(title, pad=60, fontsize=14)

    # Налаштування відступів
    plt.subplots_adjust(bottom=0.25, left=0.15, right=0.85, top=0.70)

    # Відобразити графік
    plt.show()

# Виводимо матриці
print("Матриця нечіткого відношення S (спеціальності x характеристики):")
print(S)
print("\nМатриця нечіткого відношення Q (характеристики x претенденти):")
print(Q)
print("\nРезультат нечіткої композиції (S ∘ Q):")
print(result)
print("\nРезультат альтернативної композиції (min-max) (S ∘ Q):")
print(alt_result)
print('\n')

# Виводимо графіки
plot_matrix(S, Y, X, "Нечітке відношення S (спеціальності x характеристики)")
plot_matrix(Q, Z, Y, "Нечітке відношення Q (характеристики x претенденти)")
plot_matrix(result, Z, X, "Результат композиції S ∘ Q")
plot_matrix(alt_result, Z, X, "Альтернативна композиція min-max (S ∘ Q)")

# Додатково вивести результати з описом спеціальностей і претендентів
for i in range(len(X)):
    for j in range(len(Z)):
        print(f"Відповідність претендента {Z[j]} спеціальності {X[i]}:")
        print(f"Максимінна композиція: {result[i, j]:.2f}, Альтернативна композиція (min-max): {alt_result[i, j]:.2f}")