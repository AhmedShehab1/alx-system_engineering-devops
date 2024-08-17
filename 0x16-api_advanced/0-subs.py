#!/usr/bin/python3
"""
returns the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    response = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json")
    if response:
        response_json = response.json()
        return response_json.get('data', {}).get('subscribers', 0)
    else:
        return 0
