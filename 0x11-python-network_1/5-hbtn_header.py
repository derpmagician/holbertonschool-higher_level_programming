#!/usr/bin/python3
"""
Sends a request to the URL and displays the value of the X-Request-Id variable
found in the header of the response.
"""

from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)

    print(req.headers.get('X-Request-Id'))
