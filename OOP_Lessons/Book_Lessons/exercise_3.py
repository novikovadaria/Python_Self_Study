"""
Упрежнения:
1. Киоск с мороженным
Напишите класс IceCreamStand, наследующий от класса Restaurant. Добавьте атрибуты с именем flavours для хранения
списка сортов мороженного. Напишите метод, который выведет этот списолк. 
Созадйте экземпляр IceCreamStand и вызовите этот метод.

2. Администратор
Напишите класс с именем Admin, наследующий от класса User. Добавьте атрибут privileges для хранения списка строк типо
"разрешено добавить сообщение", "разрешено банить" и т.д
Напишите метод show_privileges() для вывод набора привелегий и создайте экземпляр класса, вызовите метод

3. Привелегии
Напишиет класс Privileges. Класс должен содержать всего один атрибут privileges со списком строк из упражнния.
Переместите в него метод show_privileges()

4. Обновление аккумулятора
Добавьте в класс Battery метод с именем upgrade_battery(). Этот метод должен проверять размер аккумулятора
и устанавливать мощность равной 100, если она имеет другое значение.

"""

# 1

class Restaurant():
    def __init__(self, rest_name, cuisine_type):
        self.rest_name = rest_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant is called  {self.rest_name}, it serves {self.cuisine_type} cuisin. Since this morning it served {self.number_served} clients")

    def set_number_served(self, new_number_served):
        self.number_served = new_number_served
    
    def open(self):
        print('Мы открыты!')

class IceCreamStand(Restaurant):
    def __init__(self, rest_name, cuisine_type, flavours):
        super().__init__(rest_name, cuisine_type)
        self.flavours = flavours

    def show_flavours(self):
        print(self.flavours)

rest = IceCreamStand('Tasty Cafe', 'Coffe Shop', ["rawsberry", "chocolate", "banana"])
rest.show_flavours()

# 2
"""
class User():
    def __init__(self, first_name, last_name, country):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        print(f"User name is {self.first_name} their last name is {self.last_name}. They are from {self.country}")

    def greet_user(self):
        print(f'Hi, {self.first_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'{self.login_attempts} login attempts')

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'{self.login_attempts} login attempts')


class Admin(User):
    def __init__(self, first_name, last_name, country, privileges):
        super().__init__(first_name, last_name, country)
        self.privileges = privileges

    def show_privileges(self):
        print(f'This user has rights to {self.privileges}') 

admin_1 = Admin('Grisha', 'Vlasov', 'Russia', ['ban a user'])
admin_1.show_privileges()
"""

# 3

class User():
    def __init__(self, first_name, last_name, country):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        print(f"User name is {self.first_name} their last name is {self.last_name}. They are from {self.country}")

    def greet_user(self):
        print(f'Hi, {self.first_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'{self.login_attempts} login attempts')

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'{self.login_attempts} login attempts')

class Privileges():
    def __init__(self):
        self.privileges = ['ban a user', 'delete messages']
    
    def show_privileges(self):
        print(f'This user has rights to {self.privileges}') 

class Admin(User):
    def __init__(self, first_name, last_name, country):
        super().__init__(first_name, last_name, country)
        self.privileges = Privileges()

admin_1 = Admin('Grisha', 'Vlasov', 'Russia')
admin_1.privileges.show_privileges()

# 4

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

    def  upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
    

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
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
