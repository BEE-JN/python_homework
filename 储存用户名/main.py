# coding=utf-8
# author:GCS


import fun


def greet_user():
    username = fun.get_stored_username()
    if username:
        print("Welcome back " + username + "!")
    else:
        username = fun.get_new_username()
        print("I'will remember you " + username + "!")


greet_user()