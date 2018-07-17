# coding=utf-8
# author:GCS


import json


file_name = "user.json"


def get_stored_username():
    try:
        with open(file_name) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("请输入你的名字：")
    with open(file_name, "w") as file:
        json.dump(username, file)
    return username