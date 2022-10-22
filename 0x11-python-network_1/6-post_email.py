#!/usr/bin/python3
"""
This script takes in a url and an email address, sends a POST
request to the passed URL with the email as a paramater
and finally displays the body of the response
"""


if __name__ == "__main__":
    from sys import argv
    from requests import get, post

    value = {'email': argv[2]}
    respo = post(argv[1], data=value)
    print(respo)
