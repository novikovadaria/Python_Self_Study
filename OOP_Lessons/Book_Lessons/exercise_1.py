"""
Упрежнения:
1. Ресторан
Создайте класс с именем Restaurant. Метод __init__() класса должен содержать два атрибута: name и cuisine_type. 
Создайте метод  description(), к-ый выводит два атрибута, и метод open(), к-ый выводит сообщение о том, что рестаран открыт.
Создайте на основе своего класса экземпляр с именем restaurant. Выведите два атрибута по отдельности, затем вызовите оба методаю.

2. Три ресторана
Начните с класса из пред упражнения. Создайте три разных экземпляра, вызовите для каждого метод describe_restaurant()

3. Пользователи
Создайте класс сименем Users. Создайте два атрибута first_name и last_name, а затем ещё несколько атрибутов, которые обычно хранятся в профиле пользователя. 
Напишите метод describe_user(), к-ый выводит сводку с информацией о пользователе.
Создайте ещё один метод greet_user() для вывода персонального приветствия для пользователя.
"""

# 1 

class Restaurant():
    def __init__(self, rest_name, cuisine_type):
        self.rest_name = rest_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is called  {self.rest_name}, it serves {self.cuisine_type} cuisin")

    def open(self):
        print('Мы открыты!')

rest1 = Restaurant('La familiar', 'European')
rest2 = Restaurant('Kasha', 'European')
rest3 = Restaurant('Shirak', 'Eastern')

# 2 

rest1.describe_restaurant()
rest2.describe_restaurant()
rest3.describe_restaurant()

# 3

class User():
    def __init__(self, first_name, last_name, country):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country

    def describe_user(self):
        print(f"User name is {self.first_name} their last name is {self.last_name}. They are from {self.country}")

    def greet_user(self):
        print(f'Hi, {self.first_name}')

user_1 = User('Trisha', 'Deker', 'USA')
user_1.describe_user()
user_1.greet_user()
