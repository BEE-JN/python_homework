# coding=utf-8
# author:GCS

# 创建一个至少包含5个用户的列表，其中一个用户名为admin
# 如果用户名为admin，就打印Hello admin,would you like to see a status report?
# 否则打印一条普通的消息
# 如果列表为空就打印消息We need ro find some users!
# 删除列表所有用户确定打印正确的消息
users = ["admin", "simba", "john", "2333", "van"]
if users:
    for user in users:
        if user == "admin":
            print("Hello admin ,would you like to see a status report?")
        else:
            print("Hello " + user + " thank you for logging in again!")
else:
    print("we need to find some users!")

while users:
    users.pop()
print(users)
if users:
    for user in users:
        if user == "admin":
            print("Hello admin ,would you like to see a status report?")
        else:
            print("Hello " + user + " thank you for logging in again!")
else:
    print("we need to find some users!")

# 创建一个包含5个用户名的列表，命名为current_users
# 再创建一个包含5个用户名的列表，命名为new_users，并确保其中有一两个用户名也包含在current_users中
# 遍历列表new_users，对于其中每个用户名都检查是否被使用过
# 确保不区分大小写
current_users = ["van", "john", "simba", "iot", "tank"]
new_users = ["John", "TANK", "boy", "next", "door"]
for new_user in new_users:
    if new_user.lower() in current_users:
        print("you cann't use " + new_user + " as your name!")
    else:
        print("are you sure to use " + new_user + "?")

# 在一个列表储存1-9，遍历这个列表，使用一个if-elif-else结构，以打印每个数字对应的序数
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in nums:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(str(num) + "th")
