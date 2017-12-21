import requests


#resp = requests.get('https://api.gdax.com/products/LTC-USD/ticker')
api_base = 'https://api.gdax.com'
response = requests.get(api_base + '/products')
print(response.json())


def products():
    response = requests.get(api_base + '/products')
    #invalid api check
    if response.status_code is not 200:
        raise Exception('Invalid GDAX Status Code: %d' % response.status_code)
    return response.json()

