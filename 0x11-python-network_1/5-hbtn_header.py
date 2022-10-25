#!/usr/bin/python3
"""
This script takes in a URL, send request to the URL
and displays the value of X-Request-Id in response header
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    respo = get(argv[1])
    print(respo.headers.get("X-Request-Id")
    respo.close()
