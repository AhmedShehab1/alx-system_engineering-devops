#!/usr/bin/python3
"""
Gathering employee data
"""

import csv
import requests
import sys

if __name__ == "__main__":
    name = None
    data = [
        ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    ]
    employee_id = sys.argv[1]

    def get_name(employee_id):
        if not name:
            json_response = get_response(f'users/{employee_id}').json()
            return json_response.get('name')
        else:
            return name

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

    for task in get_tasks_dict(employee_id):
        temp_list = [f"{employee_id}", f"{get_name(employee_id)}",
                     f"{task.get('completed')}", f"{task.get('title')}"]
        data.append(temp_list)
    with open(f'{employee_id}.csv', mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(data)
