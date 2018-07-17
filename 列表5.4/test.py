#以特殊的方式跟管理员打招呼：
# users = ["admin","Simba","John","Marry","Lucy"]
# if users:
#     for user in users:
#         if user == "admin":
#             print("Hello admin,would you like to see a status report?")
#         else:
#             print("hello " + user + ",thank you for logging in again")
# else:
#     print("We need to find some users")

#检查用户名
current_users = ["school","sky","flight","easy","van"]
new_users = ["sky","ktv","boy","next","door","van"]
for new_user in new_users:
    if new_user.lower() in current_users:
        print("You can not use " + new_user + " as your name!")
    else:
        print("You can use " + new_user + " as your name!")