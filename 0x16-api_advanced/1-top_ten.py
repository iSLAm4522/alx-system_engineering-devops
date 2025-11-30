#!/usr/bin/python3
""" script that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {"limit": 10}
    response = requests.get(
        url=url,
        allow_redirects=False,
        headers=headers,
        params=params
    )
    if response.status_code != 200:
        print(None)
        return
    posts = response.json()
    for post in posts["data"]["children"]:
        print(post["data"]["title"])
