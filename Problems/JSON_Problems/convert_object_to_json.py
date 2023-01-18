import json
from json import JSONDecoder


class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

vehicle = Vehicle('Toyota Rav4', '2.5L', 32000)

class VehicleEncoder(JSONDecoder):
    def default(self, o):
        return o.__dict__

vehicle_json = json.dumps(vehicle, indent=4, cls=VehicleEncoder)
