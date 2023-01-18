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