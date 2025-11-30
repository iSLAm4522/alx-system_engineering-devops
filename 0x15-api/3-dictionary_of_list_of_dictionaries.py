#!/usr/bin/python3
"""
3-dictionary_of_list_of_dictionaries.py

This module retrieves and exports information about all employees'
TODO lists using a REST API (https://jsonplaceholder.typicode.com).
It fetches data for all users and their tasks, then exports them to
a JSON file in a structured format.

Usage:
    ./3-dictionary_of_list_of_dictionaries.py
"""

if __name__ == '__main__':
    import json
    import requests

    base_url = 'https://jsonplaceholder.typicode.com'
    session = requests.Session()

    # Get all users
    users_resp = session.get(f"{base_url}/users")
    users = users_resp.json()

    # Get all todos
    todos_resp = session.get(f"{base_url}/todos")
    todos = todos_resp.json()

    # Create a dictionary to store all employee data
    all_employees_data = {}

    # Process each user
    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # Get all tasks for this user
        user_tasks = [task for task in todos if task.get("userId") == user_id]

        # Format tasks according to requirements
        formatted_tasks = []
        for task in user_tasks:
            formatted_tasks.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        # Add to main dictionary with user_id as key
        all_employees_data[str(user_id)] = formatted_tasks

    # Export to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employees_data, json_file)
    session.close()
