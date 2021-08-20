#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter, and
finally displays the body of the response.
"""

from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    payload = {'email': argv[2]}
    req = requests.post(url, data=payload)

    print(req.text)
