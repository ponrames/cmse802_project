import requests
from bs4 import BeautifulSoup
import os
import zipfile
import pandas as pd

url = "http://mis.nyiso.com/public/P-58Blist.htm"

payload = {}
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Cookie': '_ga=GA1.1.1107251991.1726950173; _ga_P5WS5K4XN5=GS1.1.1729274664.3.1.1729274901.0.0.0',
  'If-Modified-Since': 'Fri, 18 Oct 2024 18:06:01 GMT',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Locate the table that appears after the specified HTML snippet
tables = soup.find_all('table')
target_table = None

prefix = "http://mis.nyiso.com/public/"
for table in tables:
    if table.find('th', text='Archived Files (zip format)'):
        target_table = table
        break

all_links = []
# Extract all links from the target table
if target_table:
    links = target_table.find_all('a')
    for link in links:
        all_links.append(prefix + link.get('href'))
else:
    print("Target table not found")

# Download, unzip, and merge CSV files
csv_files = []
for link in all_links:
    file_url = link
    file_name = link.split('/')[-1]
    if("2022" in file_name):
            break

    if 'zip' in file_name:
        # Download the zip file
        print(f"Downloading {file_url}...")
        r = requests.get(file_url)
        with open(file_name, 'wb') as f:
            f.write(r.content)
        
        # Unzip the file
        print(f"Unzipping {file_name}...")
        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall('.')
            csv_files.extend(zip_ref.namelist())
        
        # Optionally, delete the zip file after extraction
        os.remove(file_name)
# Merge all CSV files into a single DataFrame
merged_df = pd.concat([pd.read_csv(f) for f in csv_files])

# Group by the 'Name' column and save each group to a unique CSV file
grouped = merged_df.groupby('Name')
for name, group in grouped:
    group.to_csv(f'{name}.csv', index=False)
    print(f"Saved {name}.csv")

for file in csv_files:
    os.remove(file)