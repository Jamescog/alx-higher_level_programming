#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request
to the passed URL with the email as parameter
and displays the body of response (decoded in utf-8)
"""


if __name__ == "__main__":
    from sys import argv
    from urllib import request, parse

    value = {'email': argv[2]}
    pars = parse.urlencode(value)
    pars = pars.encode('utf-8')
    req = request.Request(argv[1], data=pars)
    with request.urlopen(req) as respo:
        content = respo.read().decode('utf-8')
    print(content)
