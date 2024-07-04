# Домашняя работа по уроку "Способы вызова функции"

# Задача "Рассылка писем"

# В программе реализована функция send_email для проверки адресов получателя и отправителя почтового сообщения
# с выводом на консоль соответствующего сообщения – об ошибке или об успешной отправке почты.

def send_email(message, recipient, *, sender="university.help@gmail.com"):
    # message – сообщение, recipient – получатель, sender – отправитель
    if not "@" in recipient or not "@" in sender \
            or not (recipient[-4:] == ".com" or recipient[-3:] == ".ru" or recipient[-4:] == ".net") \
            or not (sender[-4:] == ".com" or sender[-3:] == ".ru" or sender[-4:] == ".net"):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса: {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса: {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

print ('\nРабота завершена.')