# изначально удов 50%
# если рыбка на 5% увелич
# если мышка на 10% увелич
# если несколько, - 15%

mood = 50


m = 10
f = 5
n = -15
fg = 10
mg = 15
fl = 3
ml = 8

while 0 < mood < 1000:
    food = input("Что ты скушал? ")

    def moodik(zhenya):
        print(f"Ты доволен на {zhenya}% !")

    if food == "рыбков" or food == "рыбу" or food == "рыбоньких" or food == "рыбов":
        amount = int(input("Сколько ты скушал? "))
        s = input("Насколько большим было лакомство? ")
        if s == "огромное" or s == "большое" or s == "гиганское" or s == "большенькое":
            mood = mood + fg * amount
            moodik(mood)

        elif s == "маленькое" or s == "малюсенькое" or s == "небольшое" or s == "крохотное":
            mood = mood + fl * amount
            moodik(mood)

        elif s == "cреднее" or s == "обычное" or s == "нормальное":
            mood = mood + f * amount
            moodik(mood)
        else:
            print("Очень необычно")

    elif food == "мыши" or food == "мышков" or food == "мышеньких" or food == "мышов":
        amount = int(input("Сколько ты скушал? "))
        s = input("Насколько большим было лакомство? ")
        if s == "огромное" or s == "большое" or s == "гиганское" or s == "большенькое":
            mood = mood + mg * amount
            moodik(mood)
        elif s == "маленькое" or s == "малюсенькое" or s == "небольшое" or s == "крохотное":
            mood = mood + ml * amount
            moodik(mood)
        elif s == s == "cреднее" or s == "обычное" or s == "нормальное":
            mood = mood + m * amount
            moodik(mood)
        else:
            print("Очень необычно")

    elif food == "ничего" or food == "ничегошеньки":
        mood = mood + n
        moodik(mood)

    else:
        print("Котики такое не едят")
