# Самостоятельная работа по уроку "Произвольное число параметров"

# Цель: закрепить знание использования параметров *args/ **kwargs на практике.

# Задача "Однокоренные"

# Написать функцию single_root_words,
#     принимающую одно обязательное слово в параметр root_word,
#         а далее неограниченную последовательность в параметр *other_words.
# Функция должна составить новый список same_words
#     только из тех слов списка other_words, которые содержат root_word
#     или, наоборот, root_word содержит одно из этих слов.
# После вернуть список same_words в качестве результата своей работы.

# Примечания:
# При проверке наличия одного слова в составе другого стоит учесть, что регистр символов не должен влиять ни на что.
#     ('Disablement' - 'Able') ('Able', 'able', 'AbLe' - все подходят)
# В этой задаче вам могут понадобиться следующие методы строк/ключевые слова:
#     а. Оператор in или count()
#     b. lower()/upper().


def single_root_words(root_word, *other_words):
    same_words=[]
    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
# >>> ['richiest', 'orichalcum', 'richies']

print(result2)
# >>> ['Able', 'Disable']

print ('\nРабота завершена.')