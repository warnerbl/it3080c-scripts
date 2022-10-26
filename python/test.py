import json, urllib.request

r = urllib.request.urlopen('https://api.wheretheiss.at/v1/satellites/25544')

data=json.load(r)

print(data)

name = data['name']
longitude = data['longitude']
latitude = data['latitude']
velocity = data['velocity']
visiblity = data['visibility']


print("Satellite name: ", name)
print("Longitude: ", longitude)
print("Latitude: ", latitude)
print("Velocity: ", velocity)
print("Visibility", visiblity)