# ---------------------------------------------------------------------------------------------
# -------------------------------------- Конструкторы -----------------------------------------
# ---------------------------------------------------------------------------------------------

class Human:
    def study(self):
        print('I study python')

# dasha = Human()
# dasha.study()

# dasha = Human( 1 , 5 ) # TypeError: Human() takes no arguments


# class Human:
#     def __init__(self, x, y):
#         pass
#     def study(self):
#         print('I study python every day')

# dasha = Human( 1 , 5 ) 



# class Human:
#     def __init__(self, x, y):
#         # Значение по умолчанию
#         self.x = 10

#         self.x = x
#         self.y = y

#     def walk(self):
#         print('Walking')

# dasha = Human(12, 11.7)
# dasha.walk()


class Human:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self):
        print(f'Walking Coordinates ({self.x}, {self.y})')

dasha = Human(12, 11.7)
dasha.walk()