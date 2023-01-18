import cmath

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a <= 0:
    print('The valua of a cannot be zero or less')
else:
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))

    descriminant = (b**2) - (4*a*c)
    answer_1 = (-b-cmath.sqrt(descriminant)) / (2*a)
    answer_2 = (-b+cmath.sqrt(descriminant)) / (2*a)

print(answer_1, answer_2)



