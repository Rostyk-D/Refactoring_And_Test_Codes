import numpy as np
import random
import time
import matplotlib.pyplot as plt

# Ініціалізація генератора випадкових чисел на основі поточного часу
random.seed(time.time())

# Списки професій, характеристик і кандидатів
professions = ["менеджер", "програміст", "водій", "секретар"]
attributes = ["гнучкість мислення", "критичне мислення", "концентрація уваги",
             "здорова пам'ять", "витривалість", "швидкість реакції рухів", "відповідальність"]
candidates = ["Андрієнко", "Василенко", "Іваненко", "Дмитренко", "Петренко", "Романенко"]

# Функція для генерації випадкової матриці

def generate_random_matrix(rows, cols):
    return np.array([[random.random() for _ in range(cols)] for _ in range(rows)])

# Генеруємо випадкові матриці нечіткого відношення
profession_attribute_matrix = generate_random_matrix(len(professions), len(attributes))
attribute_candidate_matrix = generate_random_matrix(len(attributes), len(candidates))

# Функція для виконання композиції нечітких відношень

def fuzzy_composition(prof_attr, attr_cand):
    composition_matrix = np.zeros((prof_attr.shape[0], attr_cand.shape[1]))
    for i in range(prof_attr.shape[0]):
        for j in range(attr_cand.shape[1]):
            composition_matrix[i, j] = np.max(np.minimum(prof_attr[i, :], attr_cand[:, j]))
    return composition_matrix

# Функція для виконання альтернативної мінімальної композиції нечітких відношень

def fuzzy_composition_minmax(prof_attr, attr_cand):
    composition_matrix = np.zeros((prof_attr.shape[0], attr_cand.shape[1]))
    for i in range(prof_attr.shape[0]):
        for j in range(attr_cand.shape[1]):
            composition_matrix[i, j] = np.min(np.maximum(prof_attr[i, :], attr_cand[:, j]))
    return composition_matrix

# Обчислюємо композиції
composition_result = fuzzy_composition(profession_attribute_matrix, attribute_candidate_matrix)
alt_composition_result = fuzzy_composition_minmax(profession_attribute_matrix, attribute_candidate_matrix)

# Функція для побудови графіка матриці

def plot_matrix(matrix, x_labels, y_labels, title):
    fig, ax = plt.subplots(figsize=(14, 12))  # розмір графіка
    cax = ax.matshow(matrix, cmap='Blues')

    # Додати кольорову шкалу
    fig.colorbar(cax)

    # Підписи осей
    ax.set_xticks(np.arange(len(x_labels)))
    ax.set_yticks(np.arange(len(y_labels)))
    ax.set_xticklabels(x_labels, fontsize=10, rotation=90, ha='right')
    ax.set_yticklabels(y_labels, fontsize=10)

    # Назва графіка
    plt.title(title, pad=60, fontsize=14)
    plt.subplots_adjust(bottom=0.25, left=0.15, right=0.85, top=0.70)
    plt.show()

# Виводимо матриці
print("Матриця нечіткого відношення (професії x характеристики):", profession_attribute_matrix)
print("\nМатриця нечіткого відношення (характеристики x кандидати):", attribute_candidate_matrix)
print("\nРезультат нечіткої композиції:", composition_result)
print("\nРезультат альтернативної композиції (min-max):", alt_composition_result, '\n')

# Відображення графіків
plot_matrix(profession_attribute_matrix, attributes, professions, "Нечітке відношення (професії x характеристики)")
plot_matrix(attribute_candidate_matrix, candidates, attributes, "Нечітке відношення (характеристики x кандидати)")
plot_matrix(composition_result, candidates, professions, "Результат композиції")
plot_matrix(alt_composition_result, candidates, professions, "Альтернативна композиція min-max")

# Вивід результатів відповідності
for i in range(len(professions)):
    for j in range(len(candidates)):
        print(f"Відповідність кандидата {candidates[j]} професії {professions[i]}:")
        print(f"Максимінна композиція: {composition_result[i, j]:.2f}, Альтернативна композиція (min-max): {alt_composition_result[i, j]:.2f}")
