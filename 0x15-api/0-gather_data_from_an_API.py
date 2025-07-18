#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

This module retrieves and displays information about an employee's
TODO list progress using a REST API[](https://jsonplaceholder.typicode.com).
It takes a user ID as a command-line argument and prints the number of
completed tasks, total tasks, and the titles of completed tasks for
the specified employee.

Usage:
    ./0-gather_data_from_an_API.py <employee_id>
"""

if __name__ == '__main__':
    import requests
    import sys

    user_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'
    session = requests.Session()

    user_resp = session.get(f"{base_url}/users/{user_id}")
    user = user_resp.json()
    employee_name = user.get("name")

    tasks_resp = session.get(f"{base_url}/todos", params={"userId": user_id})
    tasks = tasks_resp.json()
    number_of_done_tasks = sum(1 for task in tasks if task.get("completed"))
    total_number_of_tasks = len(tasks)

    print(
        f"Employee {employee_name} is done with tasks"
        f"({number_of_done_tasks}/{total_number_of_tasks}):"
    )
    done_tasks = [task.get("title") for task in tasks if task.get("completed")]
    for title in done_tasks:
        print(f"\t {title}")
