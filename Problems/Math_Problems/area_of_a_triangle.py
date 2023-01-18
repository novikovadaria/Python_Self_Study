# Using the Heron's Formula

side_1 = int(input('Side One: '))
side_2 = int(input('Side Two: '))
side_3 = int(input('Side Three: '))

semi_perimeter = (side_1 + side_2 + side_2)/2
area = (semi_perimeter - side_1)*(semi_perimeter-side_2)*(semi_perimeter - side_3) ** 0.5
print(area)