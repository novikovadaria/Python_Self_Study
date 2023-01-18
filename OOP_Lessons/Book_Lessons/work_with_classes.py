# --------------------------------------------------------------------------------------------
# ------------------------------ Работа с классами и экземлярами -----------------------------
# --------------------------------------------------------------------------------------------

"""
class Car():

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Значение по умолчанию

    def get_descriptive_name(self):

        long_name = f'{self.year} {self.make} {self.model}'
        return long_name

    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it')

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

"""

# -------------------------------------------------------------------------------------------------
# --------------------------------------- Изменения значения атрибута -----------------------------
# -------------------------------------------------------------------------------------------------

# Прямое изменение атрибута 

"""
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
"""

# Изменение значения атрибута при помощи метода

class Car():

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Значение по умолчанию

    def get_descriptive_name(self):

        long_name = f'{self.year} {self.make} {self.model}'
        return long_name

    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading: # Расширение метода 
            self.odometer_reading = mileage
        else:
            print('You cant roll back on odometer!')

    # Изменение с приращиванием
    def increment_odometer(self, miles):
        
        # Увеличивает показатели
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_used_car = Car('subary', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.increment_odometer(100)

my_used_car.read_odometer()

