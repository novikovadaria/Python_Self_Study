# ---------------------------------------------------------------------------------------------
# --------------------------- Арифметческие операции -----------------------------------------
# ---------------------------------------------------------------------------------------------

class Human:
    coordinate_z = 45.87 

    def __init__(self, x, y): 
        self.x = x 
        self.y = y

    def __add__(self, other):                                           # <-------- __add__
        return f'Coordinates {self.x + other.x} and {self.y + self.y}'

    def __sub__(self, other):                                           # <-------- __sub__
        return f'Coordinates {self.x - other.x} and {self.y - self.y}'

    def __mul__(self, other):                                           # <-------- __mul__
        return f'Coordinates {self.x * other.x} and {self.y * self.y}'
    
    def __floordiv__(self, other):                                      # <-------- __floordiv__
        return f'Coordinates {self.x // other.x} and {self.y // self.y}'


dasha = Human(4.08, 3.08)
masha = Human(4.08, 3.08)

print(dasha + masha)
print(dasha - masha)
print(dasha *  masha)
print(dasha // masha)