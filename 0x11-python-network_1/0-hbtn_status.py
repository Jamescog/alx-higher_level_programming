#!/usr/bin/python3
"""
This script fetchs  https://alx-intranet.hbtn.io/status
The package used: urllib
"""

from urllib import response


if __name__ == "__main__":
    from urllib import request
    with request.urlopen("https://alx-intranet.hbtn.io/status") as r:
        binary = r.read()
        ty = type(binary)
        m = r.msg
        print("Body response:")
        print("    - type: {}".format(ty))
        print("    - content: {}".format(binary))
        print("    - utf8 content: {}".format(m))
