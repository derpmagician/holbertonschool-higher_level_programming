#!/usr/bin/python3
"""
Sends a POST request to the URL with the email as a parameter, and displays the
body of the response (decoded in utf-8).
"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    url = argv[1]
    data = urlencode({'email': argv[2]}).encode('ascii')
    req = Request(url, data)

    with urlopen(req) as res:
        print(res.read().decode('utf-8'))
