#!/usr/bin/python3
"""
This script takes in GitHub username and password and uses
the GitHub API to display the id of user
"""


if __name__ == "__main__":
    from requests import get, auth as a
    from sys import argv
    auth = a.HTTPBasicAuth(argv[1], argv[2])
    api_root = 'https://api.github.com/user'
    r = get(api_root, auth=auth)
    response = r.json()
    print(response.get("id"))