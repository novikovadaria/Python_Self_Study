# запрос
# преобразуем в список с помощью list()
# выдаём случайный элемент
import random

smt = 999
while 0 < smt < 1000:

    choice = input("Введите то, что из чего выбираете:\n")
    choice_list = choice.split()
    answer = random.choice(choice_list)
    print(answer)
