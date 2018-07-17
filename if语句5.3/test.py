# coding=utf-8
# author:GCS

# 假设在游戏中射杀了一个外星人，创建一个名为alien_color的变量，并将其设置为'green','yellow'或者'red'
# 编写if语句，检查外星人是否是绿色的，如果是就打印一条消息，指出玩家获得了5个点
# 如果是黄色的就打印一条消息指出玩家获得了10个点
# 如果外星人是红色的就打印一条消息指出玩家获得了15个点
alien_color = 'yellow'
if alien_color == 'green':
    print("you get 5 points")
elif alien_color == 'yellow':
    print("you get 10 points")
else:
    print("you get 15 points")

# 创建一个列表名为favorite_fruits，其中包含你最喜欢的3种水果
# 编写5条if语句，每条都检查某种水果是否包含在列表中，如果包含就打印语句
favorite_fruits = ["bananas", "apples", "watermanlens"]
if "bananas" in favorite_fruits:
    print("you really like bananas!")
if "chiken" in favorite_fruits:
    print("you really like chicken!")
if "apples" in favorite_fruits:
    print("you really like apples!")
