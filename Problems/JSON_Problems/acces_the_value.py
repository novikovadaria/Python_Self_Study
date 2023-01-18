import json

data = """{1:'one', 2:'two', 3:'three'}"""

data = json.loads(data)
print(data[2])