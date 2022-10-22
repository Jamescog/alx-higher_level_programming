#!/usr/bin/python3
"""
Get latest 10 commits from given owner and repo
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    repo = argv[1]
    owner = argv[2]
    api_root = f"https://api.github.com/repos/{owner}/{owner}/commits"
    res = get(api_root)
    res = res.json()
    for i in range(10):
        sha = res[i].get("sha")
        name = (res[i].get("commit").get("author").get("name"))
        print("{}: {}".format(sha, name))
