#!/usr/bin/python3
"""
Gathering employee data
"""

import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    def get_name(employee_id):
        json_response = get_response(f'users/{employee_id}').json()
        return json_response['name']

    def get_response(route_to_append):
        return requests.get(f'https://jsonplaceholder.typicode.com/\
        {route_to_append}')

    def get_tasks_dict(employee_id):
        tasks = get_response(f'todos?userId={employee_id}')
        return tasks.json()

    def get_done_tasks_title(employee_id):
        done_tasks = []
        tasks_dict = get_tasks_dict(employee_id)
        for task in tasks_dict:
            if task['completed']:
                done_tasks.append(task['title'])
        return done_tasks

    print(f'Employee {get_name(employee_id)} is done with tasks\
    ({len(get_done_tasks_title(employee_id))}\
    /{len(get_tasks_dict(employee_id))}):')
    for task_title in get_done_tasks_title(employee_id):
        print(f' \t{task_title}')
