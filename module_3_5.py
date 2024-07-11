# Самостоятельная работа по уроку "Рекурсия"

# Цель: применить знания о рекурсии в решении задачи.

# Задача "Рекурсивное умножение цифр"

# Написать функцию get_multiplied_digits,
#     принимающую целое число в качестве параметра number
#     и подсчитывающую произведение цифр этого числа.

# Стек вызовов будет выглядеть следующим образом:
# get_multiplied_digits(40203) -> 4 * get_multiplied_digits(203) -> 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3


def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0: 1])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(40203)

print(result)
# >>> 24

print ('\nРабота завершена.')