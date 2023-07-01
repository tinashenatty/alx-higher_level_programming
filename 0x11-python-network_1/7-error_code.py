#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response."""
if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    res = requests.get(url)
    status_code = res.status_code
    if status_code >= 400:
        print(f"Error code: {status_code}")
    else:
        print(res.text)

