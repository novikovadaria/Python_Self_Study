while True:
    class Mouse():
        def sound():
            print('*rustle*')

        def hide():
            print('I must be carefull or this stupid cat wiil catch me!')

        def save():
            print('Oh no!')
            print('*Started runnimg away*')
            print('Hahaha you cant eat me! You too slow!')

        def not_save():
            print('Oh no!')
            print('Dont eat me, please! I am a good mouse!')
            print('*A kitty has eaten you!*')

    class Kitty:
        def sound():
            print('Meow-meow')

        def hunt():
            print('A mouse!')
            print('*A kitty started folowing a mouse.*')

        def good_hunt():
            print('Catch you! You are my supper now!')
            print('Yummy!')
            print('*sounds of chewing*')
            print('*swallowed*')

        def bad_hunt():
            print('Oh no! She is running away!')
            print('My supper! Wait!')
            print('*Mouce has run away*')
            print('i am sad and hungry.')

    point = 0

    char = input('Choose a character. You want be a kitty or a mouse?\n')
    if char == 'kitty':
        point += 10
        Kitty.sound()
        print('*suddenly you saw a mouse.*')
        Kitty.hunt()
        action = input('Obviously, you want to catch it. But you are just a kitty and you have never hunted on your own.\nWhich one strategy will you choose:\n  1.watch carefully and  attack unexpectedly\n  2.just chase after it\n')
        if action == '1':
            point += 10
            Kitty.good_hunt()
            print('Congratulations! You won!')
            print('You have got', point, 'points')
        elif action == '2':
            point -= 5
            Kitty.bad_hunt()
            print('You lost.')
            print('You have got', point, 'points')
        else:
            print('Please enter a number of your choice')
    elif char == 'mouse':
        point += 20
        Mouse.sound()
        print('*You are walking in the hight grass hoping nobody can see you. You have just stolen a piece of cheese and feel pround about it*')
        Mouse.hide()
        print('*Suddenly you saw big and scary cat with a long tail and sharp teeth*')
        m_action = input('Obviously, you dont want to be eaten by a cat.\nMoreover you know that you are faster and smaller that them.\nSo which one strategy will you choose:\n  1.run away quickly\n  2.come closer and observe\n')
        if m_action == '1':
            point += 5
            Mouse.save()
            print('Congratulations! You won!')
            print('You have got', point, 'points')
        elif m_action == '2':
            point -= 20
            Mouse.not_save()
            print('You are dead.')
            print('You have got', point, 'points')
        else:
            print('Please enter a number of your choice')
    else:
        print('Please choose one character from the suggested ones.')
