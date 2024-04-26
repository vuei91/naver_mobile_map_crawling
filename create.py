import json

import requests

with open("hospitals2.json", 'r') as f:
    filters = json.load(f)

for filter in filters:
    requests.post("http://localhost:8080/hospital/", json=filter, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJuYXZlcl9uanhDTnlLN2VVbGtOQiIsImlhdCI6MTcxNDAzOTQ1MCwiZXhwIjoxNzE0MDQzMDUwfQ.JDsZNcfnSUukkAffoUu8VBLhhoY70CSYH-TOJJ6FRug'})
