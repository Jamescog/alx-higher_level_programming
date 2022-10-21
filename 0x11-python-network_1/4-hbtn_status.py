#!/usr/bin/python3
"""
This script fetchs https://alx-intranet.hbtn.io/status
using the package request
"""


if __name__ == "__main__":
    from requests import get
    with get("https://alx-intranet.hbtn.io/status") as respo:
        print("""Body response:
    - type: {}
    - content: {}""".format(type(respo.text), respo.text))
