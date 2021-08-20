#!/usr/bin/python3
"""
Sends request to URL and displays the value of the X-Request-Id variable found
in the header of the response.
"""

from sys import argv
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = argv[1]
    req = Request(url)

    with urlopen(req) as res:
        headers = res.info()
        print(headers.get('X-Request-Id'))
