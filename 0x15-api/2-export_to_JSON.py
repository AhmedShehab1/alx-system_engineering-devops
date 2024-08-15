#!/usr/bin/python3
"""
Gathering employee data
"""

import json
import requests
import sys

if __name__ == "__main__":
    name = None
    data = []
    employee_id = sys.argv[1]

    def get_username(employee_id):
        global name
        if not name:
            json_response = get_response(f'users/{employee_id}').json()
            name = json_response.get('username')
        return name

    def get_response(route_to_append):
        return requests.get(f'https://jsonplaceholder.typicode.com/\
{route_to_append}')

    def get_tasks_dict(employee_id):
        tasks = get_response(f'todos?userId={employee_id}')
        return tasks.json()

    def save_json_format():
        with open(f"{employee_id}.json", mode='w', encoding='utf-8')\
                  as json_file:
            json_file.write(json.dumps({employee_id: get_list()}))

    def get_list():
        temp_list = []
        for task in get_tasks_dict(employee_id):
            temp_dict = {'task': task.get('title'), 'completed':
                         task.get('completed'),
                         'username': get_username(employee_id)}
            temp_list.append(temp_dict)
        return temp_list
    save_json_format()
