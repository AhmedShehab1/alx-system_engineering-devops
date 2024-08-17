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
    if not response:
        print('None')
        return
    try:
        response_json = response.json()
        posts = response_json.get('data', {}).get('children', [])
        if not posts:
            print('None')
            return
        for post in posts:
            print(post.get('data', {}).get('title'))
    except Exception:
        print('None')
