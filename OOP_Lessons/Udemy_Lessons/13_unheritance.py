# -------------------------------------------------------------------------------------------
# ------------------------------------ Наследование -----------------------------------------
# -------------------------------------------------------------------------------------------
"""
# Родительский класс
class Human:
    def sing(self):
        print('La-la-la')


# Саб классы
class Jane(Human):
    def jog(self):
        print('Jogging')

class John(Human):
    def run(self):
        print('Running')


runner = John()
jogger = Jane()
jogger.sing()
jogger.jog()
runner.run()
runner.sing()
"""

# -------------------------------------------------------------------------------------------
# ------------------------- Наследование атрибутов класса -----------------------------------
# -------------------------------------------------------------------------------------------

class Person:
    def __init__(self):
        self.employed = True


class Jane(Person):
    def jog(self):
        print('Jogging')

class John(Person):
    def run(self):
        print('Running')

runner = John()
jogger = Jane()

print(runner.employed)
print(jogger.employed)