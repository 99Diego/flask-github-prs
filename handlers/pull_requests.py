import os
import requests

TOKEN = os.getenv("TOKEN")
HEADERS = {"Authorization": f"Bearer {TOKEN}"}
URL = "https://api.github.com/repos/boto/boto3/pulls"

def get_pull_requests(state):
    """
    Example of return:
    [
        {"title": "Add useful stuff", "num": 56, "link": "https://github.com/boto/boto3/pull/56"},
        {"title": "Fix something", "num": 57, "link": "https://github.com/boto/boto3/pull/57"},
    ]
    """

    # Write your code here
    params = {"state": state, "per_page": 100}
    response = requests.get(URL, headers=HEADERS, params=params)

    data = response.json()

    pull_requests = []
    for pr in data:
        pull_requests.append({        
            "num": pr["number"],
             "title": pr["title"],
             "Link": pr["html_url"]
    })

    return pull_requests
