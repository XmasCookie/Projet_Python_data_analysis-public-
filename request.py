import requests
import json

#Demande d'un résultat à travers l'API
url = 'http://localhost:5000/api'

data = [[0.0001,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002]]
j_data = json.dumps(data)

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)