#!/usr/bin/python3
"""Python script that fetches a url"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url).text
    print("Body response:")
    print(f"\t- type: {type(response)}")
    print(f"\t- content: {response}")
