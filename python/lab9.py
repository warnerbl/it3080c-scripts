
import json 
import requests

r = requests.get('http://localhost:3000')
data = r.json()
jsonData = json.loads(r.text)

print(data)
for i in jsonData: 
    print(i['name'],'is', i['color'])
