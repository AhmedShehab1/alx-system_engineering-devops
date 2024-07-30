#!/usr/bin/python3
"""
Gathering employee data
"""
import json
import requests

if __name__ == "__main__":
    name = None
    data = []
    employee_id = None

    def get_username(id):
        global employee_id
        global name
        if employee_id != id:
            json_response = get_response(f'users/{id}').json()
            name = json_response.get('username')
            employee_id = id
        return name

    def get_response(route_to_append):
        return requests.get(f'https://jsonplaceholder.typicode.com/\
{route_to_append}')

    def get_tasks_dict(employee_id):
        tasks = get_response(f'todos?userId={employee_id}')
        return tasks.json()

    def get_employee_list(id):
        employee_list = []

        def get_dict():
            for task in get_tasks_dict(id):
                employee_dict = {}
                employee_dict.update({"username": get_username(id)})
                employee_dict.update({"task": task.get('title')})
                employee_dict.update({"completed": task.get('completed')})
                employee_list.append(employee_dict)
        get_dict()
        return employee_list

    result = {}
    for i in range(1, 11):
        result.update({f'{i}': get_employee_list(i)})

    with open('todo_all_employees.json', mode='w',
              encoding='utf-8') as json_file:
        json_file.write(json.dumps(result))
