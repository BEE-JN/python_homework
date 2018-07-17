y = int(input("请输入年："))
m = int(input("请输入月："))
d = int(input("请输入日："))

if m == 1 or m == 2:
    m += 12
    y -= 1

week = int((d+2*m+3*(m+1)/5+y+int(y/4)-int(y/100)+int(y/400))%7)

if week == 0:
    print("今天是星期一")
if week == 1:
    print("今天是星期二")
if week == 2:
    print("今天是星期三")
if week == 3:
    print("今天是星期四")
if week == 4:
    print("今天是星期五")
if week == 5:
    print("今天是星期六")
if week == 6:
    print("今天是星期天")
