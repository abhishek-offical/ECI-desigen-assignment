# Write a Python program that write data in csv file using Pandas of ISS location with timestamp min 100 records
# use this url to get the data of ISS
# ( url : http://api.open-notify.org/iss-now.json)

import requests
import pandas as pd
import time

# Set the API endpoint URL
url = "http://api.open-notify.org/iss-now.json"

# Create a list to store the data
data = []

# Fetch the data and write to CSV file
while len(data) < 100:
    response = requests.get(url)
    if response.status_code == 200:
        iss_data = response.json()
        timestamp = iss_data["timestamp"]
        latitude = iss_data["iss_position"]["latitude"]
        longitude = iss_data["iss_position"]["longitude"]
        data.append([timestamp, latitude, longitude])
        print(f"Record {len(data)}: Timestamp={timestamp}, Latitude={latitude}, Longitude={longitude}")
        time.sleep(1)  # wait for 1 second before fetching next record
    else:
        print("Failed to retrieve data:", response.status_code)
        break

# Create a Pandas DataFrame from the data
df = pd.DataFrame(data, columns=["Timestamp", "Latitude", "Longitude"])

# Write the DataFrame to a CSV file
df.to_csv("iss_location_data.csv", index=False)

print("Data written to iss_location_data.csv")