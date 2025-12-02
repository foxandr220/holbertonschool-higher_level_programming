#!/usr/bin/python3
"""Search API: send POST request with letter q"""

import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": q}

    try:
        r = requests.post(url, data=payload)
        data = r.json()
    except Exception:
        print("Not a valid JSON")
        sys.exit(0)

    if not data:
        print("No result")
    else:
        print("[{}] {}".format(data.get("id"), data.get("name")))
