#!/usr/bin/python3
"""
This script fetchs  https://alx-intranet.hbtn.io/status
The package used: urllib
"""

if __name__ == "__main__":
    from urllib import request

    r = request.urlopen("https://alx-intranet.hbtn.io/status")
    print("""Body response:
        - type: {}
        - content: {}
        - utf8 content: {}""".format(type(r.peek()), r.peek(), r.msg))
