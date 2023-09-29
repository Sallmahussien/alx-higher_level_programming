#!/usr/bin/python3
"""
    Python script that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
    found in the header of the response.
"""

import sys
from urllib.request import urlopen

if __name__ == "__main__":
    url = sys.argv[1]

    with urlopen(url) as response:
        pass

    print(response.getheader("X-Request-Id"))
