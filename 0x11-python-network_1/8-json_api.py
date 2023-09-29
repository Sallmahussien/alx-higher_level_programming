#!/usr/bin/python3
"""
    Python script that takes in a letter and sends a POST request to a give url
    with the letter as a parameter.
"""

import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    post_dict = {"q": sys.argv[1] if len(sys.argv) > 1 else ""}

    response = requests.post(url, data=post_dict)

    try:
        json_data = response.json()

        if json_data == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_data["id"], json_data["name"]))
    except ValueError:
        print("Not a valid JSON")
