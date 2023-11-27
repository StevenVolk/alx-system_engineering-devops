#!/usr/bin/python3
"""

Python script to export data to json file

"""
from requests import get
from sys import argv
from json import dump


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = get(url + "users").json()
    with open("todo_all_employees.json", "w") as f:
        dump({user["id"]: [{"task": task["title"],
             "completed": task["completed"], "username": user["username"]}
              for task in get(url + "users/{}/todos"
                              .format(user["id"])).json()]
              for user in users}, f)
