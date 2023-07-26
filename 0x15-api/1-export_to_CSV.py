#!/usr/bin/python3
"""

Python script to export data to CSV file

"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    u_id = argv[1]
    username = get(url + "users/{}".format(u_id)).json().get("username")
    todo_list = get(url + "users/{}/todos".format(u_id)).json()
    with open("{}.csv".format(u_id), "w") as f:
        for task in todo_list:
            file.write("'{}','{}','{}','{}'\n".format(u_id, username,
                       task.get("completed"), task.get("title")))
