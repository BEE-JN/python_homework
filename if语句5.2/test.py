# coding=utf-8
# author:GCS

import random

# 条件测试，每个测试以及你对其结果都打印出来
car = "subaru"
print("Is car=='subaru'? I predict True")
print(car == 'subaru')

print("\nIs car=='audo'? I predict False")
print(car == 'audo')

# 检查两个字符串是否相等
string1 = "boy next the door"
string2 = "boy next the door"
if string1 == string2:
    answer = "相同"
else:
    answer = "不相同"
print("\n两个字符串" + answer)

# 使用函数lower()的测试
current_users = ["simba", "susan", "marry"]
new_users = ["MARRY", "LUCY"]
for new_user in new_users:
    if new_user.lower() in current_users:
        print("\nYou cann't use " + new_user)

# 检查两个数字相等，不等，小于，大于，等于，小于等于
num1 = 5
num2 = 3
num3 = 8
num4 = 5
print("\nnum1<num2? ")
print(num1 < num2)
print("\nnum1=num4?")
print(num1 == num4)

# 使用关键字and和or的测试
grade = random.randint(10, 100)
if grade < 60:
    level = "不及格"
elif grade >= 60 and grade < 90:
    level = "良好"
else:
    level = "优秀"
print("\n" + level + "\n")

# 测试特定的值是否在列表中
array1 = [3, 6, 9, 1, 5]
array2 = [6, 4, 8, 0, 1]
for num in array2:
    if num in array1:
        print("num " + str(num) + " in array1")
