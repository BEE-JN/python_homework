# coding=utf-8
# author:GCS


import json


file_name = "test.json"
with open(file_name) as file:
    nums = json.load(file)
print(nums)