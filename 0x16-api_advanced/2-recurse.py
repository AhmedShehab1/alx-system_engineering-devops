#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles
for a given subreddit.
"""
import requests


list_data = []


def recurse(subreddit, hot_list=[]):
    global list_data
    if len(hot_list) == 0:
        response = requests.get(f"https://www.reddit.com/r/\
{subreddit}/hot.json?show=all")
        response_json = response.json()
        if not response:
            return None
        list_data = response_json.get('data').get('children')

    if list_data == []:
        return hot_list
    hot_list.append(list_data.pop(0).get('data').get('title'))
    return recurse(list_data[len(hot_list):], hot_list)
