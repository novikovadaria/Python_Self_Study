year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('leap lear')
        else:
            print('not leap')
else:
    print('not leap')

