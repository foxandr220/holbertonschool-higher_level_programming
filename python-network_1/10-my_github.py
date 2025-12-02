#!/usr/bin/python3
"""Use GitHub API to display user id"""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]   # this must be your personal access token

    url = "https://api.github.com/user"

    r = requests.get(url, auth=(username, password))

    try:
        data = r.json()
    except Exception:
        print("None")
        sys.exit(0)

    print(data.get("id"))
