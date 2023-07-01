#!/usr/bin/python3
"""github api"""
if __name__ == '__main__':
    import requests
    import sys

    username = sys.argv[1]
    passwd = sys.argv[2]

    headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {passwd}",
            "X-GitHub-Api-Version": "2022-11-28"
            }
    res = requests.get("https://api.github.com/user", headers=headers)
    user = res.json()
    print(user.get('id'))
