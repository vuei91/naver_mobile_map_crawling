import json

import requests

with open("hospitals2.json", 'r') as f:
    filters = json.load(f)

for filter in filters:
    requests.post("http://localhost:8080/hospital/", json=filter, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJuYXZlcl9uanhDTnlLN2VVbGtOQiIsImlhdCI6MTcxNjM2MTMyMiwiZXhwIjoxNzE2MzY0OTIyfQ.n0YSCRPLE1nltPpze_B-JfEr2kPm0bT_eFG6kOfi49Q'})


































