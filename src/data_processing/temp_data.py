import requests
import os


import pandas as pd
from datetime import datetime

url = "https://api.oikolab.com/weather?param=temperature&param=wind_speed&lat=40.6501&lon=-73.9496&start=2023-01-01&end=2024-11-18&param=total_precipitation"

payload = 'param=temperature&param=wind_speed&lat=23.1&lat=42.1&lon=114.1&lon=-79.3&location_id=store1&location_id=store2&start=2022-01-01&end=2022-12-31'
headers = {
  'api-key': os.getenv("API_KEY")
}

data = requests.request("GET", url, headers=headers, data=payload)


data=dict(data["data"])


print(data["columns"])
print(data["index"])
print(data["data"])

#print(a["data"])



columns = data["columns"]
index = data["index"]
values = data["data"]
index = [datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') for ts in index]


ss="(-73.9496, -79.3)"

df = pd.DataFrame(values, columns=columns, index=index)

df = df.drop(df[df.score < 50].index)


csv_file_path = 'output.csv'
df.to_csv(csv_file_path)

print(f"CSV file created at: {csv_file_path}")