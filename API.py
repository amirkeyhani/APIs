import requests

base_url = 'https://api.openweathermap.org/data/2.5/weather?'
api_key = 'e3272f9f4db81f7c0f10e6e9e3dabbcc'
city = input('Enter city name: ')
URL = f'{base_url}q={city}&units=imperial&appid={api_key}'
response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    main = data['main']
    print(f'Temperature: {main["temp"]}')
    print(f'Min Temp: {main["temp_min"]}')
    print(f'Max Temp: {main["temp_max"]}')
    print(f'Humidity: {main["humidity"]}')
else:
    print('City not found')

# response = requests.get('https://randomuser.me/api/')
# print(response.status_code)
# print(response.json())