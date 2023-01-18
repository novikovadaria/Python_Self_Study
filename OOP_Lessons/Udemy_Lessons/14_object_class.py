# -------------------------------------------------------------------------------------------
# ------------------------------------ Класс Объект -----------------------------------------
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

# Проверка экземпляра на принадлежность к родительскому классу и саб классу
print(isinstance(runner, John))
print(isinstance(runner, Person))

# Всё в питоне это экземпляр класса object
print(isinstance(Person, object))

# Проверка на саб класс
print(issubclass(John,  Person))
print(issubclass(John,  object))
