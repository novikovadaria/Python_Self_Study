import json

{'name':'Toyota Rav4', 'engine':'2.5L', 'price':32000}

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

vehicle = Vehicle('Toyota Rav4', '2.5L', 32000)

def vehicle_decoder(obj):
    return Vehicle(obj['name'], obj['engine'], obj['price'])

vehicle = json.loads({'name':'Toyota Rav4', 'engine':'2.5L', 'price':32000}, object_hook=vehicle_decoder)
