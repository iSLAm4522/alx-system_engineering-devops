#!/usr/bin/python3
""" script that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url=url, allow_redirects=False, headers=headers)
    if response.status_code != 200:
        return 0
    data = response.json()
    return data.get("data").get("subscribers")
