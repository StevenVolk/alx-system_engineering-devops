#!/usr/bin/python3
"""

using this REST API, for a given employee ID,
returns information about his/her TODO list progress

"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    u_id = argv[1]
    user = get(url + "users/{}".format(u_id)).json().get('name')
    todo_list = get(url + "users/{}/todos".format(u_id)).json()
    tasks = [task.get("title") for task in todo_list if task["completed"]]
    print("Employee {} is done with tasks({}/{}):"
          .format(user, len(tasks), len(todo_list)))
    for task in tasks:
        print("\t {}".format(task))
