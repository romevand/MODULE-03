# Дополнительное практическое задание по модулю: "Подробнее о функциях"

# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности.

# Задача "Раз, два, три, четыре, пять .... Это не всё?"

# Написать функцию get_multiplied_digits,
#     для подсчёта суммы всех чисел и длин всех строк.

# Что должно быть подсчитано:
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)


def calculate_structure_sum(data):
    if isinstance(data, int):
        return data
    if isinstance(data, str):
        return len(data)
    if isinstance(data, (list, tuple)):
        if len(data) == 0:
            return 0
        return calculate_structure_sum(data[0]) + calculate_structure_sum(data[1:])
    if isinstance(data, set):
        return calculate_structure_sum(list(data))
    if isinstance(data, dict):
        return calculate_structure_sum(list(data.items()))


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)

print(result)
# >>> 99

print ('\nРабота завершена.')