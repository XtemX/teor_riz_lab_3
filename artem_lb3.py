import math
import pandas as pd


def utility_function(x):
    return math.sqrt(x + 5) / 15.0


outcomes = [10, -5, -5]  # Варіанти прибутків (desyatky tys. $)
probabilities = [0.5, 0.1, 0.4]  # Ймовірності станів середовища

decisions = {
    "Рішення I": [10, -5, -5],
    "Рішення II": [-5, -5, 10],
    "Рішення III": [1.5, 1.5, 0],
    "Рішення IV": [0, 0, 0],
}

results = {}

for name, matrix in decisions.items():
    expected_utility = 0.0
    for val, prob in zip(matrix, probabilities):
        u_val = utility_function(val)
        expected_utility += prob * u_val
    results[name] = expected_utility

# 4. Формування та вивід таблиці результатів
df_results = pd.DataFrame(
    list(results.items()), columns=["Рішення", "Сподівана корисність M(U)"]
)

df_results = df_results.sort_values(
    by="Сподівана корисність M(U)", ascending=False
).reset_index(drop=True)

print("ТАБЛИЦЯ РЕЗУЛЬТАТІВ")
print(df_results.to_string(index=False))

print("\n--- ВИСНОВОК ---")
best_decision = df_results.iloc[0]["Рішення"]
best_val = df_results.iloc[0]["Сподівана корисність M(U)"]
print(
    f"Найбільш ефективним за концепцією Неймана є {best_decision} з M(U) ≈ {best_val:.5f}."
)