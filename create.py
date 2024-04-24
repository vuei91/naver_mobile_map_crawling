import json

import requests

with open("hospitals.json", 'r') as f:
    filters = json.load(f)

for filter in filters:
    requests.post("http://localhost:8080/hospital/", json=filter)
