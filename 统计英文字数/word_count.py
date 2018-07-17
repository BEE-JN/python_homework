# coding=utf-8
# author:GCS


def count_word(file_name):
    try:
        with open(file_name) as f_n:
            contents = f_n.read()
    except FileNotFoundError:
        print("找不到" + file_name)
    else:
        words = contents.split()
        num = len(words)
        print(words)
        print("文件有" + str(num) + "个英文单词")
