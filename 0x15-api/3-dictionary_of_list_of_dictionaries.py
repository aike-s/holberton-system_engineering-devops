#!/usr/bin/python3
"""
Using a REST API return information about an employee
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    user_id = 1
    all_employee_tasks = {}

    json_file = "todo_all_employees.json"

    while user_id <= 10:
        user_response = requests.get("https://jsonplaceholder" +
                                     ".typicode.com/users?id=" + str(user_id))

        user_name = user_response.json()[0]["name"]
        user_username = user_response.json()[0]["username"]

        todos_response = requests.get("https://jsonplaceholder" +
                                      ".typicode.com/todos?userId=" +
                                      str(user_id))
        todos = todos_response.json()

        total_num_tasks = 0
        num_done_tasks = 0
        user_done_tasks = []
        user_all_tasks = []

        for task in todos:
            if task["completed"] is True:
                num_done_tasks = num_done_tasks + 1
                user_done_tasks.append(task["title"])

            """ For .json file """
            user_all_tasks.append(dict({"username": user_username,
                                        "task": task["title"],
                                        "completed": task["completed"]}))

            total_num_tasks = total_num_tasks + 1

        all_employee_tasks[user_id] = user_all_tasks

        user_id = user_id + 1

    with open(json_file, 'w+') as open_file:
        json.dump(all_employee_tasks, open_file)

    print("Employee {} is done with tasks({}/{}):".format(user_name,
                                                          num_done_tasks,
                                                          total_num_tasks))
    for task in user_done_tasks:
        print("\t {}".format(task))
