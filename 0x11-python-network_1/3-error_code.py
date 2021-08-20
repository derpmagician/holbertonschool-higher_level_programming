#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response in utf-8 also
handles HTTPError exceptions to print the HTTP Status Code, if an error occurs.
"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError


if __name__ == "__main__":
    url = argv[1]
    req = Request(url)

    try:
        with urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as ex:
        print('Error code:', ex.code)
