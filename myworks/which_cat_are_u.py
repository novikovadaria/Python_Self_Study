
pen = 0
act = 0
laz = 0

while True:
    a = input("Ты часто грустишь? ")
    if a == "да":W
        pen += 10
    elif a == "нет":
        act += 10
    elif a == "возможно":
        laz += 10
    else:
        print("Ты можешь отвечать только 'да', 'нет', 'возможно'. ")

    b = input("Ты любишь заниматься спортом? ")
    if b == "да":
        act += 10
    elif b == "нет":
        laz += 10
    elif b == "возможно":
        pen += 10
    else:
        print("Ты можешь отвечать только 'да', 'нет', 'возможно'. ")

    c = input("Ты много леженькаешь? ")
    if c == "да":
        laz += 10
    elif c == "нет":
        act += 10
    elif c == "возможно":
        pen += 10
    else:
        print("Ты можешь отвечать только 'да', 'нет', 'возможно'. ")

    d = input("Ты любишь шутонькие? ")
    if d == "да":
        act += 10
    elif d == "нет":
        pen += 10
    elif d == "возможно":
        laz += 10
    else:
        print("Ты можешь отвечать только 'да', 'нет', 'возможно'. ")

    e = input("Ты часто бросаешь начатое?  ")
    if e == "да":
        laz += 10
    elif e == "нет":
        act += 10
    elif e == "возможно":
        pen += 10
    else:
        print("Ты можешь отвечать только 'да', 'нет', 'возможно'. ")

    f = input("Ты любишь гоняться за мышков или выслеживать птиченьких? ")
    if f == "да":
        act += 10
    elif f == "нет":
        laz += 10
    elif f == "возможно":
        pen += 10
    else:
        print("Ты можешь отвечать только 'да', 'нет', 'возможно'. ")

    g = input("Ты часто бываешь задумчивым? ")
    if g == "да":
        pen += 10
    elif g == "нет":
        laz += 10
    elif g == "возможно":
        act += 10
    else:
        print("Ты можешь отвечать только 'да', 'нет', 'возможно'. ")

    h = input("У тебя много идей, которые ты стремишься реализовать? ")
    if h == "да":
        act += 10
    elif g == "нет":
        laz += 10
    elif g == "возможно":
        pen += 10
    else:
        print("Ты можешь отвечать только 'да', 'нет', 'возможно'. ")

    i = input("Ты полненький? ")
    if i == "да":
        laz += 10
    elif g == "нет":
        act += 10
    elif g == "возможно":
        pen += 10
    else:
        print("Ты можешь отвечать только 'да', 'нет', 'возможно'. ")

    j = input("Ты счастливый котик? ")
    if j == "да" or j == "нет" or j == 'возможно':
        laz += 10
        pen += 10
        act += 10
    else:
        print("Ты можешь отвечать только 'да', 'нет', 'возможно'. ")

    if pen > laz and pen > act:
        print(f"Ты на {pen}% меланхоличный котик!")
    elif laz > pen and laz > act:
        print(f"Ты на {laz}% ленивый котик!")
    elif act > pen and act > laz:
        print(f"Ты на {act}% активный котик!")
    else:
        print("Ты можешь отвечать только 'да', 'нет', 'возможно'. ")
