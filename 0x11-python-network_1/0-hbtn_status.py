#!/usr/bin/python3
"""
This script fetchs  https://alx-intranet.hbtn.io/status
The package used: urllib
"""


from urllib import request


respo = request.urlopen("https://alx-intranet.hbtn.io/status")
print("""Body response:
    - type: {}
    - content: {}
    - utf8 content: {}""".format(type(respo.peek()), respo.peek(), respo.msg))

