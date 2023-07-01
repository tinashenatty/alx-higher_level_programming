#!/usr/bin/python3
"""list 10 commits"""
if __name__ == '__main__':
    import requests
    import sys

    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo_name}/commits"
    query_string = "?per_page=10"
    headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            }
    res = requests.get(url + query_string, headers=headers)
    commits = res.json()
    for commit in commits:
        print(f"{commit.get('sha')}: "
              f"{commit.get('commit').get('author').get('name')}")
