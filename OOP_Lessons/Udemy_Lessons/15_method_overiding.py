# -------------------------------------------------------------------------------------------
# ------------------------------------ Переопределение метода -------------------------------
# -------------------------------------------------------------------------------------------

"""
class Person:
    def __init__(self):
        self.employed = True
    
    def sing(self):
        print('la-la-la')

class John(Person):
    # Переопределение метода
    def __init__(self):
        self.jogger = True
    
    def run(self):
        print('running')

runner = John()

print(runner.jogger)
print(runner.employed) # AttributeError: 'John' object has no attribute 'employed'
"""

class Person:
    def __init__(self):
        self.employed = True
    
    def sing(self):
        print('la-la-la')

class John(Person):
    def __init__(self):
        super().__init__()
        self.jogger = True
    
    def run(self):
        print('running')


runner = John()

print(runner.jogger)
print(runner.employed)