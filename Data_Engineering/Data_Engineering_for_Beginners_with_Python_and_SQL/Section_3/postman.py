import requests
import pandas as pd

url = "https://api.artic.edu/api/v1/artworks"

payload = {}
headers = {}

response = requests.request ("GET", url, headers=headers, data=payload)

# print(response.text)

data = response.json()

df = pd.DataFrame(data['data'])

print(df.columns)