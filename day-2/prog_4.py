# Write a Python program using the requests module to send a GET request to a given below URL API endpoint and print the json response
# (Url : http://api.open-notify.org/iss-now.json

import requests
import json

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print("Failed to retrieve data:", response.status_code)