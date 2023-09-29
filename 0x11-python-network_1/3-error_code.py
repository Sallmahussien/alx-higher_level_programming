#!/usr/bin/python3
"""
    Python script that takes in a URL, sends a request to the URL
    and displays the body of the response (decoded in utf-8).
"""

import sys
from urllib.request import urlopen
from urllib.error import HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as error:
        print("Error code: {}".format(error.status))
