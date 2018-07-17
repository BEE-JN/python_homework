# coding=utf-8
# author:GCS

# 使用字典来储存一个人的信息，包括姓，名，年龄和居住的城市
person = {
    'name': '郭崇山',
    'age': 19,
    'city': '株洲',
}
print(person)

# 使用一个字典来储存一些人喜欢的数字
favorite_num = {
    'boy': 1,
    'next': 2,
    'the': 3,
    'door': 4,
}
print(favorite_num)

# 想出5个编程词汇，并用作词典中的键，他们的含义作值储存在字典中
# 用整洁的方法打印出每个词汇及其含义

words = {
    'print': '打印',
    'sort': '排序',
    'pop': '弹出元素',
    'remove': '移除元素',
}
for key, value in words.items():
    print(key + ":" + value)

# 创建一个字典，在其中储存3条河流及其经过的国家
rivers = {
    'nile': 'egypt',
    'changjiang': 'china',
    'huanghe': 'china' ,
}
for key, value in rivers.items():
    print("The " + key.title() + " runs through " + value.title())
for key in rivers.keys():
    print(key.title())
for value in rivers.values():
    print(value)

# 最喜欢的语言
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
should_take = ['jen','boy','sarah','van','simba']

for people in should_take:
    if people in favorite_languages.keys():
        print("Thank you for taking," + people)
    else:
        print("Please take it," + people)