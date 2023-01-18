import requests

client_id = 'PrxHU_0RcUqkwNl71KJajg'
api_key = 'n0xrUDrRpGBJ6814TRwl9WEafU8uvXs2LagqaSzrhsGcdV6LHg3mbtx4B6pR2kCjtiFpuwY4LjXZYo22OIu-BihaSJ2QqxET9hPdZmcLpLa_FObbyJ78Ul480aHvYnYx'
api_url = 'https://api.yelp.com/v3/businesses/search'

headers = {
    'Authorization': 'Bearer ' + api_key
}
params = {
    'term': 'IT',
    'limit': 30,
    'location': 'Russia'
}

response = requests.get(api_url, headers=headers, params=params)
businesses = response.json()['businesses']
for business in businesses:
    print(business['name'])
