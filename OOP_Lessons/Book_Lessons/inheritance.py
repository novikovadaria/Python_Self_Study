# --------------------------------------------------------------------------------------------
# ------------------------------ Наследование ------------------------------------------------
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

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading: # Расширение метода 
            self.odometer_reading = mileage
        else:
            print('You cant roll back on odometer!')

    # Изменение с приращиванием
    def increment_odometer(self, miles):
        
        # Увеличивает показатели
        self.odometer_reading += miles

class Batery():

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

class ElectricCar(Car):

    # Представляет аспекты машины, специфические для элеткромобилей
    def __init__(self, manufacture, model, year):
        super().__init__(manufacture, model, year)
        self.battery_size = 75

    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')

    def fill_gas_tank(self):
        print('This car doesnt have a gas tank')

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
"""

# -------------------------------------------------------------------------------------------------------
# ------------------------------ Экземпляры как атрибуты ------------------------------------------------
# -------------------------------------------------------------------------------------------------------

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


class Battery():

    def __init__(self, battery_size=75):
        self.battery_size = battery_size
            
    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')
    
    def get_range(self):

        if self.battery_size == 75:
            range = 60
        
        elif self.battery_size == 100:
            range = 315

        print(f'This car can go about {range} miles on a full charge')
    

class ElectricCar(Car):

    # Представляет аспекты машины, специфические для элеткромобилей
    def __init__(self, manufacture, model, year):
        super().__init__(manufacture, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print('This car doesnt have a gas tank')

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
