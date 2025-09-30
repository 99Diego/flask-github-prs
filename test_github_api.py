import os
import requests

TOKEN = os.getenv("TOKEN")
headers = {"Authorization": f"token {TOKEN}"}
url = "https://api.github.com/repos/boto/boto3/pulls"

response = requests.get(url, headers=headers, params={"state": "open", "per_page": 5})

print("Status:", response.status_code)
print("Response:")
print(response.json())

