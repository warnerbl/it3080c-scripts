import json 
import requests


print('Please enter your zip code: ')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=http://api.openweathermap.org/data/2.5/weather?zip=12345,us&appid=8CF0F29E6E981E877FD42AB2F9BC292D' % zip)
data = r.json()

print(data)
print(data['weather'][0]['description'])
