#!/usr/bin/python3
"""
1-export_to_CSV.py

This module exports employee data to a CSV file with
all fields enclosed in double quotes.

Usage:
    ./1-export_to_CSV.py <employee_id>
"""

if __name__ == '__main__':
    import requests
    import sys
    import csv
    user_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'
    session = requests.Session()

    user_resp = session.get(f"{base_url}/users/{user_id}")
    user = user_resp.json()
    user_name = user.get("username")

    tasks_resp = session.get(f"{base_url}/todos", params={"userId": user_id})
    tasks = tasks_resp.json()

    with open(f'{user_id}.csv', mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            row = [user_id, user_name, task.get("completed"),
                   task.get("title")]
            writer.writerow(row)
