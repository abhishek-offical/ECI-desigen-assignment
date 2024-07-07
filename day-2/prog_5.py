# Write a Python program using the requests module to send a GET request to a given below url API endpoint and print the
#  a) Latitude
#  b) Longitude
#  c) timestamp
# (url : http://api.open-notify.org/iss-now.json)

import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    iss_position = data["iss_position"]
    print("Latitude:", iss_position["latitude"])
    print("Longitude:", iss_position["longitude"])
    print("Timestamp:", data["timestamp"])
else:
    print("Failed to retrieve data:", response.status_code)