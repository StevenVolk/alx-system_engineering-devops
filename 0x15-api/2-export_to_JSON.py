#!/usr/bin/python3
"""

Python script to export data to json file

"""
from requests import get
from sys import argv
from json import dump


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    u_id = argv[1]
    username = get(url + "users/{}".format(u_id)).json().get("username")
    todo_list = get(url + "users/{}/todos".format(u_id)).json()
    with open("{}.json".format(u_id), "w") as f:
        dump({u_id: [{"task": task["title"],
             "completed": task["completed"], "username": username}
              for task in todo_list]}, f)
