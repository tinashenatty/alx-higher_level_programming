#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user with the
letter as a parameter."""
if __name__ == '__main__':
    import requests
    import sys

    q = ""
    if len(sys.argv) >= 2:
        q = sys.argv[1]
    res = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        result = res.json()
    except Exception:
        print("Not a valid JSON")
        sys.exit(1)
    if len(result) == 0:
        print("No result")
    else:
        print(f"[{result.get('id')}] {result.get('name')}")
