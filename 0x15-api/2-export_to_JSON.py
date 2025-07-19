#!/usr/bin/python3
"""
2-export_to_JSON.py

This module exports employee task data to a JSON file.

Usage:
    ./2-export_to_JSON.py <employee_id>
"""

import json
import requests
import sys

if __name__ == '__main__':

    user_id = str(sys.argv[1])
    base_url = 'https://jsonplaceholder.typicode.com'
    session = requests.Session()

    user_resp = session.get(f"{base_url}/users/{user_id}")
    user = user_resp.json()
    user_name = user.get("username")

    tasks_resp = session.get(f"{base_url}/todos", params={"userId": user_id})
    tasks = tasks_resp.json()

    new_tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user_name
        } for task in tasks
    ]

    data = {user_id: new_tasks}
    with open(f"{user_id}.json", mode='w') as file:
        json.dump(data, file)
