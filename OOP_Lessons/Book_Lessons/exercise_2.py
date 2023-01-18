"""
Упрежнения:
1. Посетители
Добавьте атрибут number_served со значением по умоланию 0; он представляет кол-во посетителей. 
Создайте экземпляр с именем restaurant. Выведите значение number_served, потом обновите и выведите снова

Добавьте метод set_number_served(), позволяющий задать кол-во обслуженных посетителей. Вызовите метод

Добавьте метод increment_number_served(), к-ый увеличивает кол-во обслуженных посетителей на заданную величину. 
Вызовите этот метод. 

2. Попытка входа: добавьте атрибут login_attempts в класс User из предыдущего задания, 
напишите метод increment_login_attempts(), увеличивающий значение login_attempts на 1. Напишите другой метод, reset_login_attempts()
обнуляющий значение login_attempts
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

restaurant = Restaurant('La familiar', 'European')

restaurant.describe_restaurant()
restaurant.set_number_served(23)
restaurant.describe_restaurant()

# 2

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
        print(f'{self.login_attempts} попыток входа')

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'{self.login_attempts} попыток входа')

user_1 = User('Trisha', 'Deker', 'USA')
user_1.describe_user()
user_1.greet_user()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()