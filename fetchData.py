import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://www.cqc.org.uk/about-us/transparency/using-cqc-data#directory'
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

# Folder name to store csv files
folder_name = "File_name"
os.makedirs(folder_name, exist_ok=True)

# Download files to folder and save the csv file locally 
csv_links = []
for link in soup.find_all('a', href=True):
    if '.csv' in link['href']:
        full_url = urljoin(url, link['href'])
        csv_links.append(full_url)

for csv_url in csv_links:
    file_name = csv_url.split("/")[-1]
    file_path = os.path.join(folder_name, file_name)
    response = requests.get(csv_url)
    
    with open(file_path, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {file_name} to {file_path}")

# Process csv file

first_file = os.path.join(folder_name, csv_links[0].split("/")[-1])

with open(first_file, 'r') as file:
    for _ in range(10):
        print(file.readline())

header_row = 4  # row index to identify header
df = pd.read_csv(first_file, header=header_row)
print(df.head())


df.reset_index(drop=True, inplace=True)

processed_file_path = os.path.join(folder_name, 'processed_' + file_name)
df.to_csv(processed_file_path, index=False)
print(f"Processed file saved as {processed_file_path}")



