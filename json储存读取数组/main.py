# coding=utf-8
# author:GCS

import json


nums = [1,2,3,4,5]
file_name = "test.json"
with open(file_name, "w") as file:
    json.dump(nums, file)