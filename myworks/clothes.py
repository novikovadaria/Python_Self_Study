# спрашиваем гендре
# спрашиваем погоду зимой
# добавляем в список одежду в зависимости от погоды зимой
# спрашиваем о спорте
# добавляем к спискам взависимости от ответа
# спрашиваем о свиданиях
# жобавляем в список в звамисимости от ответа и гендера
# печатаем финальный список

# добавлять сумму взависимости от погоды зимой
# добавлем сумму взависимости от ответа
#


b = 999
while 0 < b < 1000:

    def final_list(smt):
        print("Вам следует взять следующие вещи: ", smt)

    def final_sum(ant):
        print("Это будет стоить:", ant, "рублей")

    cold = ["Тёплая куртка", "Шерстяные носки", " Меховые сапоги", "Шапка"]
    light = ["Куртка", "Носки", 'Шапка', "Штаны"]
    sport = ["Cпортивный костюм", "Кросовки"]
    date_m = ['Классический костюм', "Туфли"]
    date_f = ["Платье", "Туфельки"]
    big_list = []

    c_w = 35000
    l_w = 8500
    s = 10000
    m_s = 15000
    f_s = 13000

    temp = int(input("Сколько обычно градусов в вашем городе зимой? "))
    if temp > 0:
        big_list = light

    elif temp < -1:
        big_list = cold

    else:
        print("Ответ дайте в числом виде")

    sport_cloth = input("Вы планируете заниматься спортом? ")
    if sport_cloth == "да":
        big_list = big_list + sport

    else:
        big_list = big_list

    gender = input('Какого вы пола? ')
    if "муж" in gender:
        big_list = big_list + date_m
        dating = input("Вы собираетесь ходить на свидания? ")
        if dating == "да":
            final_list(big_list)
        elif dating == "нет":
            big_list.remove("Туфли")
            big_list.remove("Классический костюм")

    elif "жен" in gender:
        big_list = big_list + date_f
        dating = input("Вы собираетесь ходить на свидания? ")
        if dating == "да":
            final_list(big_list)
        elif dating == "нет":
            big_list.remove("Туфельки")
            big_list.remove("Платье")
            final_list(big_list)
    else:
        final_list(big_list)
