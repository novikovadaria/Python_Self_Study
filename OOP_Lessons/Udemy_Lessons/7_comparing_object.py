# ---------------------------------------------------------------------------------------------
# --------------------------- Cравнение экземпляров с помощью магических методов --------------
# ---------------------------------------------------------------------------------------------

class Human:
    def __init__(self, x, y): 
        self.x = x 
        self.y = y

    def __eq__(self, other): # <------------- __eq__
        return self.x == other.x and self.y == other.y

    def __gt__(self, other): # <------------- __gt__
        return self.x > other.x and self.y >  other.y

    def __lt__(self, other): # <-------------  __lt__
        return  self.x < other.x and self.y <  other.y


dasha = Human(4.08, 3.08)
masha = Human(4.08, 3.08)

print(dasha == masha)
print(dasha < masha)