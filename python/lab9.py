
import json 
import requests

r = requests.get('http://localhost:3000')
data = r.json()
jsonData = json.loads(r.text)

print(data)
print("this sucks")
for i in jsonData: 
    print(i['name'],'is', i['color'])
