#!/usr/bin/python3
"""
    Lists the latest 10 commits of a specific repository by a specific user,
    using the GitHub API
"""

import sys
import requests

if __name__ == "__main__":
    owner = sys.argv[2]
    repo_name = sys.argv[1]
    url = f"https://api.github.com/repos/{owner}/{repo_name}/commits"

    response = requests.get(url).json()

    commits_list = []
    for commit in response:

        commit_dict = {
            "sha": commit.get("sha"),
            "author": commit.get("commit").get("author").get("name"),
            "time": commit.get("commit").get("author").get("date")
        }
        commits_list.append(commit_dict)

    sorted_commits = sorted(commits_list,
                            key=lambda x: x['time'],
                            reverse=True)

    for idx in range(min(10, len(sorted_commits))):
        sha = sorted_commits[idx].get("sha")
        author = sorted_commits[idx].get("author")
        print("{}: {}".format(sha, author))
