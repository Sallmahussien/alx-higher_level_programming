#!/usr/bin/python3
"""
    Python script that takes your GitHub credentials and uses
    the GitHub API to display your id
"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))
    print(response.json().get("id"))
