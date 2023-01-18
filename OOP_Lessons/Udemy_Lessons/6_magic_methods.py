# ---------------------------------------------------------------------------------------------
# --------------------------- Маджик методы ---------------------------------------------------
# ---------------------------------------------------------------------------------------------

# __str__

class Human:
    def __init__(self, x, y): 
        self.x = x 
        self.y = y

    def __str__(self):
        return f'Im a magic method with coordinates ({self.x}, {self.y})'

    def walk(self):                        
        print(f'Walking Coordinates ({self.x}, {self.y})')

test_walk = Human(0,0)
print(test_walk)