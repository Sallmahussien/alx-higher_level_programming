#!/usr/bin/python3
"""
    Python script that takes in a URL and an email,
    sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""

from urllib.request import urlopen
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    post_data = ("email=" + sys.argv[2]).encode("utf-8")

    with urlopen(url, post_data) as response:
        body = response.read()

print(body.decode("utf-8"))
