#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response in utf-8 with
requests module.
"""

from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)

    if req.status_code >= 400:
        print('Error code:', req.status_code)
    else:
        print(req.text)
