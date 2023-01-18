# ---------------------------------------------------------------------------------------------
# --------------------------- Методы экземпляра и Методы класса ---------------------------
# ---------------------------------------------------------------------------------------------

class Human:
    coordinate_z = 45.87 

    def __init__(self, x, y): 
        self.x = x 
        self.y = y

    # Декоратор
    @classmethod
    def specific_coordinate(cls):           # <------------ Метод класса
        return cls(1.1, 4.6)

    def walk(self):                         # <------------ Метод экземпляра
        print(f'Walking Coordinates ({self.x}, {self.y})')

test_walk = Human.specific_coordinate()
test_walk.walk()
