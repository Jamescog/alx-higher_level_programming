#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the
URL and displays the body of response

It manages urllib.error.HTTPErorr exceptions
and print: Error code: followed by the HTTP states code
"""

if __name__ == '__main__':
    from sys import argv
    from urllib import request as r, error as e

    try:
        with r.urlopen(argv[1]) as respo:
            print(respo.read().decode('utf-8'))
    except e.HTTPError as er:
        print("Error code: {}".format(er.code))
