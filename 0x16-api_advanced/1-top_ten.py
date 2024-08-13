#!/usr/bin/python3
"""
prints the titles of the first
10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    response = requests.get(f"https://www.reddit.com/r/{subreddit}\
/hot.json?limit=10")
    if response.status_code == 200:
        response_json = response.json()
        for post in response_json.get('data').get('children'):
            print(post.get('data').get('title'))
    else:
        print(None)
