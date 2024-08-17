#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles
for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'

    if after:
        url += f'&after={after}'
    response = requests.get(url, headers=headers)
    if not response:
        return None

    response_json = response.json()
    posts = response_json.get('data', {}).get('children', [])
    for post in posts:
        hot_list.append(post.get('data').get('title'))
    after = response_json.get('data', {}).get('after')
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
