# Пространство имён.

# Задача "Счётчик вызовов"

# В программе реализован счётчик вызовов всех каких-либо функций, вызываемых в процессе её выполнения.

calls = 0

def count_calls ():
    # Данная функция выполняет подсчёт вызовов любых функций, вызываемых процессе выполнения главной программы.
    global calls
    calls += 1

def string_info (string):
    # Данная функция вычисляет длину входной строки и переводит входную строку в верхний и нижний регистр.
    count_calls ()
    tuple = (len (string), string.upper (), string.lower ())
    return (tuple)

def is_contains (string, list_to_search):
    # Данная функция проверяет присутствие входной строки во входном списке, игнорируя при этом регистр.
    count_calls ()
    if string.lower () in (i.lower () for i in list_to_search):
        return (True)
    else:
        return (False)

print (string_info ('Capybara'))
print (string_info ('Armageddon'))
print (is_contains ('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print (is_contains ('cycle', ['recycling', 'cyclic']))    # No matches
print (calls)

print ('\nРабота завершена.')