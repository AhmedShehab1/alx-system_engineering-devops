#!/usr/bin/python3
"""
prints the titles of the first
10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(f"https://www.reddit.com/r/{subreddit}\
/hot.json?limit=10", headers=headers)
    try:
        response_json = response.json()
        for post in response_json.get('data', {}).get('children', []):
            print(post.get('data', {}).get('title'))
    except Exception:
        print('None')
