import json

data = {2:'one', 1:'two', 3:'three'}

with open('sample_json.json', 'w') as file:
    json.dump(data, file, indent=4, sort_keys= True)