#!/usr/bin/python3
"""
Write a Python script that takes your GitHub (username and password) and uses
the GitHub API to display your id
"""
from sys import argv
import requests as req

if __name__ == "__main__":
    usr = argv[1]
    pwd = argv[2]
    url = 'https://api.github.com/user'
    auth = req.auth.HTTPBasicAuth(usr, pwd)
    res = req.get(url, auth=auth)
    dobj = res.json()
    print(dobj.get('id', None))
