from_num = int(input())
to_num = int(input())


for number in range(from_num, to_num + 1):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            print(number)