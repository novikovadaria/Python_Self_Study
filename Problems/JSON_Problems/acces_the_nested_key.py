import json

data = """{
    'company':{
        'employee'{
            'name':'emma',
            'payble':{
                'salary':7000,
                'bonus':800
            }
        }
    }
}
"""

data_json = json.loads(data)
print(data['company']['employee']['payble']['salary'])