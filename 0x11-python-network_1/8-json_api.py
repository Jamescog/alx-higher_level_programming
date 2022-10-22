#!/usr/bin
#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


if __name__ == "__main__":
    from requests import post
    from sys import argv

    if len(argv) == 2:
        letter = {'q': argv[1]}
    else:
        letter = {'q': "''"}

    r = post("http://0.0.0.0:5000", data=letter)
    try:
        r = r.json()
        if len(r) == 0:
            print("No result")
        else:
            print("[{}] {}".format(r.get("id"), r.get("name")))
    except ValueError:
        print("Not a valid JSON")
