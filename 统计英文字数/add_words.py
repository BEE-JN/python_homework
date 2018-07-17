# coding=utf-8
# author:GCS


def add_words(file_name):
    with open(file_name, "a") as f_n:
        inf = input("你想输入的英文：")
        f_n.write(inf + ".\n")
