#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL
and displays the response

The response contain the value of X-Request-Id of header of the reponse
"""

if __name__ == "__main__":
    from sys import argv
    from urllib import request

    with request.urlopen(argv[1]) as respo:
        headers = dict(respo.getheaders())
    print(headers.get("X-Request-Id"))
