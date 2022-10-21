#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
and displays the body of the response

if the HTTP status code is greater than or equal 400
it will print Error code: followed by the value of the
HTTP statuse code
"""


if __name__ == "__main__":
    from sys import argv
    from requests import get
    r = get(argv[1])
    if (r.ok):
        print(r.content)
    else:
        print(f"Error code: {r.status_code}")
